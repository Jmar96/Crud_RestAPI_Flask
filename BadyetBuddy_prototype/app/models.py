from . import db
from datetime import datetime

class Badyet_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(200))
    category = db.Column(db.String(90))
    length = db.Column(db.String(90))
    amount = db.Column(db.Float)
    owner_id = db.Column(db.Integer)

class Badyet_Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(200))
    password = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


