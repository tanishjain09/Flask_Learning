from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer,primary_key=True)
    usename = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.username},Role: {self.role}>'

    def get_id(self):
        return self.uid
