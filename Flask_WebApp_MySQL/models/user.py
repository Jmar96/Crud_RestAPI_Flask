from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(90),nullable=False,unique=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200))
    created_at = db.Column(db.DateTime(),nullable=False,server_default=db.func.now())
    modified_at = db.Column(db.DateTime(),nullable=False,server_default=db.func.now(), onupdate=db.func.now())

    @property
    def data(self):
        return{
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'password':self.password
        }
    def save(self):
        db.session.add(self)
        db.session.commit()