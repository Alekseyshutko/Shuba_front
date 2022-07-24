from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel as PyModel, Extra


class BaseModel(PyModel):
    id: Optional[int]
    created: Optional[datetime]
    modified: datetime = None

    def dict_without_none(self, **kwargs):
        return self.dict(exclude_none=True, **kwargs)


class OrderAdd(BaseModel):
    title: str
    description: str
    city: str
    name: str
    phonenumber: str
    price: float
    date_finish: date
    speciality: str
    photo: str

    class Config:
        extra = Extra.ignore


class Order(BaseModel):
    pass


class CommentAdd(BaseModel):
    body = str

class Comment(BaseModel):
    pass
