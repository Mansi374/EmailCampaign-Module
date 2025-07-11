from flask import Flask
from config import Config  # from root of the project
# from flask_migrate import Migrate
from dotenv import load_dotenv
from main.extensions import db,migrate
from .models import User

load_dotenv()

# Import all your blueprints
from main.routes.email_routes import email_bp           

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set secret key for sessions
    app.secret_key = app.config.get("SECRET_KEY", "fallback_secret")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    app.register_blueprint(email_bp)       

    return app
