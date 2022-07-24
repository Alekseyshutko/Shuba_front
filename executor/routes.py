from flask import Blueprint, redirect, render_template, url_for, request
from contact.forms import ContactForm
from contact.utils import create_contact
import requests


executor_blueprint = Blueprint(
    "executor",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/executor",
)
API = "http://127.0.0.1:8000"


@executor_blueprint.route("/execut", methods=["GET", "POST"])
def exec():
    filter_spec = request.args.get("speciality")
    if filter_spec:
        a = requests.get(f"{API}/api/executor/?speciality={filter_spec}").json()
    else:
        a = requests.get(f"{API}/api/executor/").json()
    b = requests.get(f"{API}/api/speciality/").json()

    return render_template("executors.html", a=a, b=b)