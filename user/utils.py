from flask import session
import requests
from .models import User
from user.models import Login, Auth

LOGIN_URL = 'http://127.0.0.1:8000/auth/users/'


def access(*args, **kwargs):
    login = Login(**kwargs)
    res = requests.post(LOGIN_URL, json=login.dict())
    auth = Auth(**res.json())
    return auth


def request_with_auth(
        method: str = None, url: str = None,
        headers: dict = None, files: dict = None,
        data: dict = None, json: dict = None,
        **kwargs, ) -> requests.Response:
    if headers is None:
        headers = {}

    auth = Auth.from_session()

    headers.update(Authorization=f"Token {auth.token}")

    req = requests.Request(
        method=method, url=url,
        headers=headers, files=files,
        data=data, json=json,
        **kwargs
    )
    r = req.prepare()
    s = requests.Session()
    return s.send(r)


def get_current_user():
    res = request_with_auth("GET")
    user = User(**res.json())
    return user
