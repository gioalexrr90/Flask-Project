from src import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(80), nullable=False)
        
def __repr__(self):
    return f'{self.full_name}'