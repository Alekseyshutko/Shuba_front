import requests
from config import Config
from order.models import OrderAdd, Order, CommentAdd, Comment, AddPhoto, Photo
from user.utils import request_with_auth


CREATE_ORDER = f"{Config.API_URL}/order/api/order/"
CREATE_COMMENT = f"{Config.API_URL}/order/api/order_comments/"
CREATE_PHOTO = f"{Config.API_URL}/order/api/orderphotos/"


def order_add(*args, **kwargs) -> Order:
    order_add = OrderAdd(**kwargs)
    res = requests.post(CREATE_ORDER, json=order_add.dict())
    # check_response_errors(res, 201)
    order = Order(**res.json())
    print(order)
    return order

def comment_add(*args, **kwargs) -> Comment:
    comment_add = CommentAdd(**kwargs)
    res = requests.post(CREATE_COMMENT, json=comment_add.dict())
    print(res)
    # check_response_errors(res, 201)
    comment = Comment(**res.json())
    return comment

def photo_add(*args, **kwargs) -> Photo:

    photo_add = AddPhoto(**kwargs)
    res = requests.post(CREATE_PHOTO, json=photo_add.dict())
    # check_response_errors(res, 201)
    photo = Photo(**res.json())
    return photo

def order_id(*args, **kwargs):
    orde = requests.get(CREATE_ORDER).json()[-1]['id']
    return orde


