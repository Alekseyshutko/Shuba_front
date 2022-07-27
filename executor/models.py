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
    photo: str
    speciality: list

    class Config:
        extra = Extra.ignore


class Executor(PyModel):
    pass










