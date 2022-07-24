import requests
from config import Config
from executor.models import Executor, RegisterExecutor


CREATE_USER_EXECUTOR = f"{Config.API_URL}/api/executor/"


def create_contact(*args, **kwargs) -> Executor:
    register_contact = RegisterExecutor(**kwargs)
    res = requests.post(CREATE_USER_EXECUTOR, json=register_contact.dict())
    # check_response_errors(res, 201)
    executor = Executor(**res.json())
    print(executor)
    return executor