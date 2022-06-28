from pydantic import BaseModel


class RegisterUser(BaseModel):
    username: str
    email: str
    password: str
    password_submit: str
