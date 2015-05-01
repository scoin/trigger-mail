from flask import Flask 
from .extensions import db, mail, migrate


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("project.config")
    with app.app_context():
        db.init_app(app)
        mail.init_app(app)
        migrate.init_app(app, db)

    from .users.models import User

    from .users.endpoints import users
    from .campaigns.endpoints import campaigns
    from .emails.endpoints import emails

    app.register_blueprint(users, url_prefix='/users')
    app.register_blueprint(campaigns, url_prefix='/campaigns')
    app.register_blueprint(emails, url_prefix='/emails')


    return app

app = create_app()
