from flask_sqlalchemy import SQLAlchemy
from main import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class ConfigurationList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    configurations = db.relationship('Configuration', backref='Configuration_list', lazy='dynamic')


class Configuration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.Text)
    isDone = db.Column(db.Boolean)
    configuration_list_id = db.Column(db.Integer, db.ForeignKey('configuration_list.id'))