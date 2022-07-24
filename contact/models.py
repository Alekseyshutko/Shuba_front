from datetime import datetime
from typing import Optional
from pydantic import BaseModel as PyModel, Extra


class BaseModel(PyModel):
    id: Optional[int]
    created: Optional[datetime]
    modified: datetime = None

    def dict_without_none(self, **kwargs):
        return self.dict(exclude_none=True, **kwargs)


class RegisterContact(BaseModel):
    first_name: str
    last_name: str
    email: str
    message: str

    class Config:
        extra = Extra.ignore


class Contact(BaseModel):
    pass


