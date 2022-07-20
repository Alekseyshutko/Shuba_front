from flask import Blueprint, redirect, render_template, url_for, request
from .forms import OrderForm
from order.aws_utils import upload_file_to_s3
import requests

order_blueprint = Blueprint(
    "order",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/order",
)
API = "http://127.0.0.1:8000"


def add_order(*args, **kwargs):
    res = requests.post(f"{API}/order/api/order/")
    return res


@order_blueprint.route("/add", methods=["GET", "POST"])
def add():
    form = OrderForm()
    if form.validate_on_submit():
        form_data = dict(form.data)
        form_data.pop("photo")
        print(request.form)
        print(request.files)
        photo = form.photo.data
        link = upload_file_to_s3(photo)
        print(link)
        form_data["photo"] = link
        # order = add_order(**form_data)
        print(form_data)
        return redirect(url_for("index"))
    return render_template("add.html", form=form)


@order_blueprint.route("/repair", methods=["GET", "POST"])
def repair():
    filter_spec = request.args.get("speciality")
    if filter_spec:
        a = requests.get(f"{API}/order/api/order/?speciality={filter_spec}").json()
    else:
        a = requests.get(f"{API}/order/api/order/").json()
    b = requests.get(f"{API}/order/api/specialityorder/").json()

    return render_template("repair.html", a=a, b=b)
