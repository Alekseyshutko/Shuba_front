import os


class Config:
    API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
