from flask_sqlalchemy import SQLAlchemy
from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Configuration(db.Model):
    id_Configuration = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    creator = db.Column(db.Text)
    date_e = db.Column(db.DateTime)
    date_m = db.Column(db.DateTime)
    id_mutable = db.Column(db.Integer)
    mutable = db.Column(db.Text)

