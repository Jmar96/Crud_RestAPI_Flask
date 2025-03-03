from . import db

class Badyet_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(200))
    category = db.Column(db.String(90))
    length = db.Column(db.String(90))
    amount = db.Column(db.Float)
