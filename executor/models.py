from typing import Optional
from flask import session
from pydantic import BaseModel as PyModel, EmailStr, Extra, validator, Field
from datetime import datetime


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


class RegisterExecutor(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    city: str

    class Config:
        extra = Extra.ignore


class RegisterSpeciality(BaseModel):
    title: list


class Executor(BaseModel):
    is_active: bool = True


class Speciality(BaseModel):
    pass

