from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.migrate import Migrate

db = SQLAlchemy()
mail = Mail()
migrate = Migrate()
