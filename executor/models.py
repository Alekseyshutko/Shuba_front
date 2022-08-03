from typing import Optional
from flask import session
from pydantic import BaseModel as PyModel, EmailStr, Extra, validator, Field
from datetime import datetime


# class BaseModel(PyModel):
#     id: Optional[int]
#     created: Optional[datetime]
#     modified: datetime = None
#
#     def dict_without_none(self, **kwargs):
#         return self.dict(exclude_none=True, **kwargs)


class RegisterExecutor(PyModel):
    user_id: int
    first_name: str
    last_name: str
    phone_number: str
    city: str
    photo: str = None
    speciality: list

    @validator('photo')
    def size_is_some(cls, v):
        if v is None:
            raise ValueError('Cannot set photo to None')
        return str(v)

    class Config:
        extra = Extra.ignore




class Executor(PyModel):
    pass


class CommentAdd(PyModel):
    body: str
    executor: int
    user: int
    is_active: bool

    class Config:
        extra = Extra.ignore


class Comment(PyModel):
    pass







