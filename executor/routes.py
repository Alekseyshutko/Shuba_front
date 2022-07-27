from flask import Blueprint, redirect, render_template, url_for, request
from executor.forms import ExecutorForm
import requests
from user.utils import get_current_user
from executor.utils import create_executor

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


@executor_blueprint.route("/addexecutor", methods=["GET", "POST"])
def add_executor():
    form = ExecutorForm()
    if form.validate_on_submit():
        user = get_current_user()
        user.store_in_session()
        form_data = dict(form.data)
        form_data['speciality'] = list(form_data['speciality'])
        form_data['user_id'] = int(user.id)
        form_data.pop("photo")
        photo = form.photo.data
        from order.aws_utils import upload_file_to_s3
        link = upload_file_to_s3(photo)
        form_data["photo"] = link
        print(form_data)
        create_executor(**form_data)

        return redirect(url_for("index"))
    return render_template("add_executor.html", form=form)