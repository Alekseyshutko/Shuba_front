import os
# from dotenv import load_dotenv


class Config:
    API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
    SECRET_KEY = os.getenv("SECRET_KEY")