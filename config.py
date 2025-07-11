import os
from dotenv import load_dotenv

load_dotenv()  # ✅ This reads .env variables when Flask starts

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

    # ✅ Email Config (read from .env)
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")

    # ✅ Optional DB config (already there)
    SQLALCHEMY_DATABASE_URI = "sqlite:///emailcampaign.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
