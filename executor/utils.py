import requests
from config import Config
from executor.models import Executor, RegisterExecutor


CURRENT_USER_URL = f"{Config.API_URL}/api/users/me/"
CREATE_USER_EXECUTOR = f"{Config.API_URL}/api/executor/"
CREATE_USER_SPECIALIYY = f"{Config.API_URL}/api/speciality/"


def create_executor(*args, **kwargs) -> Executor:
    register_contact = RegisterExecutor(**kwargs)
    res = requests.post(CREATE_USER_EXECUTOR, json=register_contact.dict())
    print(res.json())
    # check_response_errors(res, 201)
    executor = Executor(**res.json())
    print(executor)
    return executor



