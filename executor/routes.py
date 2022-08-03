from flask import Blueprint, redirect, render_template, url_for, request
from executor.forms import ExecutorForm, CommentForm
import requests
from user.utils import get_current_user,user_retrieve_request
from executor.utils import create_executor, executor_retriev, comment_add



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


@executor_blueprint.route("/<int:id>", methods=["GET", "POST"])
def one_executor(id):
    executor = executor_retriev(id)
    form = CommentForm()
    if form.validate_on_submit():
        user = user_retrieve_request(id)
        # user.store_in_session()
        form_data = dict(form.data)
        form_data['user_id'] = int(id)
        form_data['executor'] = executor['user_id']
        form_data['user'] = form_data["user_id"]
        form_data['is_active'] = True
        comment_add(**form_data)

    com = requests.get(f'{API}/api/executor_comments/').json()
    comments = []
    for i in range(len(com)):
        if com[i]['executor'] == executor['user_id']:
            comments.append(com[i])

    return render_template("one_executor.html", executor=executor, comments=comments, form=form)


# @executor_blueprint.route("/<int:id>", methods=["GET", "POST"])
# def one_executor(id):
#     executor = executor_retriev(id)
#     form = CommentForm()
#     if form.validate_on_submit():
#         user = get_current_user()
#         user.store_in_session()
#         form_data = dict(form.data)
#         form_data['user_id'] = int(user.id)
#         form_data['user'] = form_data["user_id"]
#         form_data['executor'] = executor['user_id']
#         form_data['is_active'] = True
#         print(form_data)
#         comment_add(**form_data)
#
#     com = requests.get(f'{API}/api/executor_comments/').json()
#     comments = []
#     for i in range(len(com)):
#         if com[i]['executor'] == executor['id']:
#             comments.append(com[i])
#
#     return render_template("one_executor.html", executor=executor, comments=comments, form=form)

