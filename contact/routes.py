from flask import Blueprint, redirect, render_template, url_for, request
from contact.forms import ContactForm
from contact.utils import create_contact
import requests


contact_blueprint = Blueprint(
    "contact",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/contact",
)
API = "http://127.0.0.1:8000"


@contact_blueprint.route("/cont", methods=["GET", "POST"])
def cont():
    form = ContactForm()
    if request.method == "POST":
        contakt = create_contact(**form.data)

        return redirect(url_for("index"))
    return render_template("contact.html", form=form)
