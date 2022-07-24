import requests
from config import Config
from contact.models import Contact, RegisterContact


CREATE_USER_CONTACT = f"{Config.API_URL}/contact/api/contact/"


def create_contact(*args, **kwargs) -> Contact:
    register_contact = RegisterContact(**kwargs)
    res = requests.post(CREATE_USER_CONTACT, json=register_contact.dict())
    # check_response_errors(res, 201)
    contact = Contact(**res.json())
    print(contact)
    return contact