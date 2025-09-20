from . import db

class Test(db.model):
    id = db.Column(db.Integer,primary_key=True)
