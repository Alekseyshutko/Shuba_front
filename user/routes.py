import requests
from flask import Blueprint, redirect, render_template, url_for, request

from user.form import RegisterUserForm
from .models import RegisterUser

user_blueprint = Blueprint("user", __name__, template_folder="templates",
                           static_folder="static",
                           url_prefix='/user', )


def create_user(*args, **kwargs):
    register_user = RegisterUser(**kwargs)
    res = requests.post('http://127.0.0.1:8000/api/v1/auth/users/', json=register_user.dict())
    return res


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()
    if request.method == 'POST':
        user = create_user(**form.data)
        print(user.json())
    return render_template("register.html", form=form)
