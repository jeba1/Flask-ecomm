from . import db
from datetime import datetime
from flask_login import UserMixin
from passlib.hash import sha1_crypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique = True, nullable=False)
    email = db.Column(db.String(255), unique = True, nullable=False)
    first_name = db.Column(db.String(255), unique = True, nullable=True)
    last_name = db.Column(db.String(255), unique = True, nullable=True)
    password = db.Column(db.String(255), unique = True, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolena, default=False)
    api_key = db.Column(db.String(255), unique = True, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def encode_api(self):
        self.api_key = sha1_crypt.hash(self.username + str(datetime.utcnow))
    def encode_password(self):
        self.password = sha1_crypt.hash(self.password)
    def __repr__(self):
        return '<User %r>' % {self.username}
    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'id': self.id,
            'api_key': self.api_key,
            'is_active': True,
            'is_admin': self.is_admin

        }
