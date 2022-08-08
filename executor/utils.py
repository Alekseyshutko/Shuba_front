import requests
from config import Config
from executor.models import Executor, RegisterExecutor, Comment, CommentAdd
from user.utils import request_with_refresh



CURRENT_USER_URL = f"{Config.API_URL}/api/users/me/"
CREATE_USER_EXECUTOR = f"{Config.API_URL}/api/executor/"
CREATE_USER_SPECIALIYY = f"{Config.API_URL}/api/speciality/"
CREATE_COMMENT = f"{Config.API_URL}/api/executor_comments/"



def create_executor(*args, **kwargs) -> Executor:
    register_contact = RegisterExecutor(**kwargs)
    res = requests.post(CREATE_USER_EXECUTOR, json=register_contact.dict())
    print(res.json())
    # check_response_errors(res, 201)
    executor = Executor(**res.json())
    print(executor)
    return executor

def executor_retriev(user_id):
    req = request_with_refresh("GET", f"{Config.API_URL}/api/executor/{user_id}")
    user_data = req.json()
    return user_data


def comment_add(*args, **kwargs) -> Comment:
    comment_add = CommentAdd(**kwargs)

    res = requests.post(CREATE_COMMENT, json=comment_add.dict())
    print(res.json())
    # check_response_errors(res, 201)
    comment = Comment(**res.json())
    return comment

