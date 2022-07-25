import json

import requests
from config import Config
from order.models import OrderAdd, Order, CommentAdd, Comment
from user.utils import request_with_auth


CREATE_ORDER = f"{Config.API_URL}/order/api/order/"
CREATE_COMMENT = f"{Config.API_URL}/order/api/order_comments/"


def order_add(*args, **kwargs) -> Order:
    order_add = OrderAdd(**kwargs)
    print(type(order_add))
    print(order_add)
    # print(order_add)
    res = requests.post(CREATE_ORDER, json=order_add.dict())
    # check_response_errors(res, 201)

    order = Order(**res.json())

    return order

def comment_add(*args, **kwargs) -> Comment:
    comment_add = CommentAdd(**kwargs)
    res = requests.post(CREATE_COMMENT, json=comment_add.dict())
    # check_response_errors(res, 201)
    comment = Comment(**res.json())
    print(comment)
    return comment