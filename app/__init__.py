from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
import os

db = SQLAlchemy()
mail = Mail()
login_manager = LoginManager()

# redirect unauthorized users to login page
login_manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__, template_folder="templates")

    # Config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev_secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Register Blueprints
    from .routes import main
    from app.auth.routes import auth

    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app