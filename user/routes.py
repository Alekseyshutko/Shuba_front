import requests
from flask import Blueprint, redirect, render_template, url_for, request, session
from .utils import access, get_current_user, create_user
from user.form import RegisterUserForm, LoginForm
from user.models import RegisterUser



user_blueprint = Blueprint(
    "user",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/user",
)
API = "http://127.0.0.1:8000"


# def create_user(*args, **kwargs):
#     register_user = RegisterUser(**kwargs)
#     res = requests.post(f"{API}/api/users/register", json=register_user.dict())
#     print(res)
#     return res


@user_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterUserForm()
    if request.method == "POST":
        user = create_user(**form.data)

        return redirect(url_for("index"))
    return render_template("register.html", form=form)


@user_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        auth = access(**form.data)
        print(auth)
        auth.store_in_session()
        user = get_current_user()
        user.store_in_session()
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@user_blueprint.route("/logout", methods=["GET"])
def logout():
    print("LOGOUT")
    session.clear()
    return redirect(url_for("index"))


@user_blueprint.route('/<username>', methods=["GET", "POST"])
def user(username):
    print(session['user']['id'])
    return render_template('user.html', user=user)