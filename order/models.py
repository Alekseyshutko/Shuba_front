from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel as PyModel, Extra


# class BaseModel(PyModel):
#     id: Optional[int]
#     created: Optional[datetime]
#     modified: datetime = None
#
#     def dict_without_none(self, **kwargs):
#         return self.dict(exclude_none=True, **kwargs)


class OrderAdd(PyModel):
    user: int
    title: str
    description: str
    city: str
    name: str
    phoneNumber: str
    price: float
    date_finish: str
    speciality: list
    photo: str

    class Config:
        extra = Extra.ignore


class Order(PyModel):
    pass


class CommentAdd(PyModel):
    body = str

class Comment(PyModel):
    pass
