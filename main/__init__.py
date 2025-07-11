from flask import Flask
from config import Config  # from root of the project
from flask_migrate import Migrate
from dotenv import load_dotenv
from main.extensions import db

# Load environment variables from .env
load_dotenv()

# Import all your blueprints
from main.routes.routes import main_bp                  # your original
from main.routes.main_routes import main_bp as main_bp_clone  # cloned
from main.routes.email_routes import email_bp           # cloned

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set secret key for sessions
    app.secret_key = app.config.get("SECRET_KEY", "fallback_secret")

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(main_bp)            # your original route
    app.register_blueprint(main_bp_clone)      # cloned main route
    app.register_blueprint(email_bp)           # email form + sender

    return app
