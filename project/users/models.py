from .. import db

class User(db.Model):
    __tablename__ = 'users'

    id              = db.Column(db.Integer, primary_key=True)
    first_name      = db.Column(db.String(31), nullable=False)
    last_name       = db.Column(db.String(31), nullable=False)
    email           = db.Column(db.String(63), index=True, nullable=False, unique=True)
    password        = db.Column(db.String(63), nullable=False)
    redirect_url    = db.Column(db.String(255))
    # key 			= db.Column(db.String(63), index=True, nullable=False, unique=True)

    def __init__(self, first_name, last_name, email, password):
    	self.first_name = first_name
    	self.last_name = last_name
    	self.email = email
    	self.password = password
    	# self.key = "SECRET KEY"