from pydantic import BaseModel, Extra

class BaseModel(PyModel):
    id: Optional[int]
    # created: Optional[datetime]
    # modified: datetime = None

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
    access: str
    refresh: str


class User(BaseModel):
    email: str
    is_active: bool = True
    is_admin: bool = False
    has_profile: bool = False
