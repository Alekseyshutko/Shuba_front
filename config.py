import os
# from dotenv import load_dotenv


class Config:
    API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")  #http://shubabackend.herokuapp.com
    SECRET_KEY = os.getenv("SECRET_KEY")
    BUCKET_NAME = os.getenv("BUCEKT_NAME", "shuba")
    S3_LOCATION = os.getenv("S3_LOCATION", "eu-central-1")