from pydantic import BaseModel, Extra


class RegisterUser(BaseModel):
    username: str
    email: str
    password: str
    password_submit: str


class Login(BaseModel):
    email: str
    password: str

    class Config:
        extra = Extra.ignore


class Auth(BaseModel):
    token: str



class User(BaseModel):
    email: str
    is_active: bool = True
    is_admin: bool = False
    has_profile: bool = False
