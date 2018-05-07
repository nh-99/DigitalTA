import datetime, uuid
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

app = Flask(__name__)
app.config.from_object(config['dev'])
db = SQLAlchemy(app)

class Assignment(db.Model):
    __tablename__ = "assignments"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100))
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    output = db.Column(db.String(1000))
    graded = db.Column(db.Boolean, default=False)
    score = db.Column(db.Float)


class HomeworkCheck(db.Model):
    __tablename__ = 'checks'
    id = db.Column(db.String(50), primary_key=True, default=str(uuid.uuid4()))
    stdin = db.Column(db.String(2000))
