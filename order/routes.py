from flask import Blueprint, redirect, render_template, url_for, request, session
import json

import user.routes
from user.utils import get_current_user
from order.forms import OrderForm, CommentForm
from order.aws_utils import upload_file_to_s3
import requests
from order.utils import order_add, comment_add, photo_add, order_id, order_retriev, order_update
from config import Config
import time
import asyncio

CREATE_ORDER = f"{Config.API_URL}/order/api/order/"
SPECIALITY_ORDER = f"{Config.API_URL}/order/api/specialityorder/"
CREATE_ORDER_COMENT = f'{Config.API_URL}/order/api/order_comments/'
CREATE_ORDER_PHOTO = f'{Config.API_URL}/order/api/orderphotos/'
DETAIL_ORDER = f'{Config.API_URL}/order/api/detailorder/'

order_blueprint = Blueprint(
    "order",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/order",
)


@order_blueprint.route("/add", methods=["GET", "POST"])
async def add():
    start_time = time.time()
    form = OrderForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        form_data.pop("photo")
        form_data['date_finish'] = str(form_data["date_finish"])
        photo = form.photo.data
        link = upload_file_to_s3(photo)
        form_data["photo"] = link
        form_data['speciality'] = list(form_data['speciality'])
        form_data['user'] = int(user.id)
        task1 = asyncio.create_task(order_add(**form_data))
        form_data['order'] = order_id()
        task2 = asyncio.create_task(photo_add(**form_data))
        await task1
        await task2
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@order_blueprint.route("/repair", methods=["GET", "POST"])
def repair():
    filter_spec = request.args.get("speciality")
    if filter_spec:
        a = requests.get(f"{Config.API_URL}/order/api/order/?speciality={filter_spec}").json()
    else:
        a = requests.get(CREATE_ORDER).json()
    b = requests.get(SPECIALITY_ORDER).json()

    return render_template("repair.html", a=a, b=b)


@order_blueprint.route("/<int:id>", methods=["GET", "POST"])
def one_order(id):
    order = order_retriev(id)
    # var = requests.get(CREATE_ORDER).json()
    # order = var[id - 1]
    form = CommentForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        form_data['user'] = int(user.id)
        form_data['order'] = order['id']
        form_data['is_active'] = True
        comment_add(**form_data)

    com = requests.get(CREATE_ORDER_COMENT).json()
    comments = []
    for i in range(len(com)):
        if com[i]['order'] == order['id']:
            comments.append(com[i])
    photo = requests.get(CREATE_ORDER_PHOTO).json()
    pho = []
    for i in range(len(photo)):
        if photo[i]['order'] == order['id']:
            pho.append(photo[i])

    return render_template("one_order.html", order=order, comments=comments, form=form, pho=pho)


@order_blueprint.route("/delete/<int:id>", methods=["GET", "POST"])
async def delete(id):
    order = order_retriev(id)
    form = OrderForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        id2 = str(id)
        form_data.pop("photo")
        form_data['date_finish'] = str(form_data["date_finish"])
        photo = form.photo.data
        link = upload_file_to_s3(photo)
        form_data["photo"] = link
        form_data['speciality'] = list(form_data['speciality'])
        form_data['user'] = int(user.id)
        form_data['order'] = order_id()
        task3 = asyncio.create_task(order_update(id2, **form_data))
        task4 = asyncio.create_task(photo_add(**form_data))
        await task3
        await task4
        return redirect(url_for("index"))
    return render_template("delete.html", form=form, order=order)


@order_blueprint.route("/delete/<int:id>/del", methods=["GET"])
def order_delete(id):

    id2 = str(id)
    DETAIL_ORDER2 = f'{DETAIL_ORDER}{id2}/'
    try:
        requests.delete(DETAIL_ORDER2)
        return redirect(url_for('user.user'))
    except:
        return "Ошибка"
