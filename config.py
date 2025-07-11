import os
from dotenv import load_dotenv

load_dotenv()  

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USERNAME") 
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = int(os.getenv("DB_PORT", 3306))

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        if DB_USER and DB_PASSWORD and DB_HOST and DB_NAME
        else "sqlite:///emailcampaign.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
