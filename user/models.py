from datetime import datetime
from typing import Optional
from flask import session
from pydantic import BaseModel as PyModel, EmailStr, Extra, validator, Field


class BaseModel(PyModel):
    id: Optional[int]
    created: Optional[datetime]
    modified: datetime = None

    def dict_without_none(self, **kwargs):
        return self.dict(exclude_none=True, **kwargs)


class StoreInSessionMixin:
    def store_in_session(self: BaseModel, **kwargs):
        session[self.__class__.__name__.lower()] = self.dict()
        session.modified = True

    @classmethod
    def from_session(cls):
        data = session.get(cls.__name__.lower())
        if data is not None:
            return cls(**data)


class ErrorModel(PyModel):
    message: str = "Something Wrong."


class RegisterUser(BaseModel):
    email: str
    password: str
    password_submit: str

    @validator("password_submit")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v

    class Config:
        extra = Extra.ignore


class Login(BaseModel):
    email: str
    password: str

    class Config:
        extra = Extra.ignore


class Auth(StoreInSessionMixin, BaseModel):
    access: str
    refresh: str


class User(StoreInSessionMixin, BaseModel):

    email: str

    is_active: bool = True
    is_superuser: bool = False
