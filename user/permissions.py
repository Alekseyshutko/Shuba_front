from functools import wraps

from flask import abort
from user.models import Auth
from user.utils import get_current_user
from user.models import User

NEED_PROFILE = "Need to create profile"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user = User.from_session()
        if user is None:
            auth = Auth.from_session()
            if auth is None:
                abort(401)
            user = get_current_user()
            user.store_in_session()
        return func(*args, **kwargs)
    return wrapper


def profile_required(func):
    @wraps(func)
    @login_required
    def wrapper(*args, **kwargs):
        user = User.from_session()
        if hasattr(user, 'has_profile'):
            if not user.has_profile:
                abort(403, NEED_PROFILE)
            return func(*args, **kwargs)
    return wrapper