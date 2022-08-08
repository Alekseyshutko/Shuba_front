from flask import session
import requests

from config import Config

# from app.utils import check_response_errors
from .models import Login, Auth, RegisterUser
from .models import User


LOGIN_URL = f"{Config.API_URL}/api/token/"
REFRESH_URL = f"{Config.API_URL}/api/token/refresh/"
CURRENT_USER_URL = f"{Config.API_URL}/api/users/me/"
CREATE_USER_URL = f"{Config.API_URL}/api/users/"


def access(*args, **kwargs) -> Auth:
    login = Login(**kwargs)
    res = requests.post(LOGIN_URL, json=login.dict())
    # check_response_errors(res, 200)
    auth = Auth(**res.json())
    return auth


def refresh() -> Auth:
    auth = Auth.from_session()
    res = requests.post(
        REFRESH_URL, headers={"Authorization": f"Bearer {auth.refresh}"}
    )
    # check_response_errors(res, 200)
    auth.access = res.json()["access"]
    return auth


def request_with_auth(
    method: str = None,
    url: str = None,
    headers: dict = None,
    files: dict = None,
    data: dict = None,
    json: dict = None,
    **kwargs,
) -> requests.Response:
    if headers is None:
        headers = {}

    auth = Auth.from_session()

    headers.update(Authorization=f"Bearer {auth.access}")

    req = requests.Request(
        method=method,
        url=url,
        headers=headers,
        files=files,
        data=data,
        json=json,
        **kwargs,
    )
    r = req.prepare()
    s = requests.Session()
    return s.send(r)


def get_current_user() -> User:
    res = request_with_auth("GET", CURRENT_USER_URL)
    print(res.content)
    # check_response_errors(res, 200)
    user = User(**res.json())
    return user


def create_user(*args, **kwargs) -> User:
    register_user = RegisterUser(**kwargs)
    print(register_user.json())
    res = requests.post(CREATE_USER_URL, json=register_user.dict())
    # check_response_errors(res, 201)
    user = User(**res.json())
    print(user)
    return user

def refresh_token_request():
    refresh_token = session["refresh"]
    req = requests.post(f"{Config.API_URL}/token/refresh/", json={
        "refresh": refresh_token
    })
    session["access"] = req.json()["access"]
    session.modified = True


def request_with_refresh(
    method: str = None, url: str = None,
    headers: dict = None, files: dict = None,
    data: dict = None, json: dict = None,
    **kwargs,
) -> requests.Response:
    res = request_with_auth(
        method=method, url=url,
        headers=headers, files=files,
        data=data, json=json,
        **kwargs
    )
    if res.status_code == 403:
        refresh_token_request()
        res = request_with_auth(
            method=method, url=url,
            headers=headers, files=files,
            data=data, json=json,
            **kwargs
        )
    return res