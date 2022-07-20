from flask import Blueprint, redirect, render_template, url_for, request
from .forms import OrderForm
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
    if request.method == "POST":
        order = add_order(**form.data)
        print(order.json())
        return redirect(url_for("index"))
    return render_template("add.html", form=form)
