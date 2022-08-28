from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel as PyModel, Extra, validator, ValidationError
from user.models import StoreInSessionMixin


class OrderAdd(PyModel, StoreInSessionMixin):
    user: int
    title: str
    description: str
    city: str
    name: str
    phone_number: str
    price: float
    date_finish: str
    speciality: list

    class Config:
        extra = Extra.ignore


class Order(PyModel):
    pass


class CommentAdd(PyModel):
    body: str
    order: int
    user: int
    is_active: bool

    class Config:
        extra = Extra.ignore


class Comment(PyModel):
    pass


class AddPhoto(PyModel):
    order: int
    photo: str = None

    @validator('photo')
    def photo_is_some(cls, v):
        if v is None:
            raise ValidationError('Cannot set photo to None')
        return str(v)

    class Config:
        extra = Extra.ignore


class Photo(PyModel):
    pass