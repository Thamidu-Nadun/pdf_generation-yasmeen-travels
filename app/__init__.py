from flask import Flask
from .extensions import db
from .routes.email_route import email_bp
from .routes.log_route import log_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(email_bp, url_prefix='/email')
    app.register_blueprint(log_bp, url_prefix='/logs')
    
    return app