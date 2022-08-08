from pydantic import BaseModel as PyModel, EmailStr, Extra, validator, Field


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







