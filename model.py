from db import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable = False)
    vid = db.Column(db.Text, unique)
    filename = db.Column(db.Text, nullable=False)
    satisfaction = db.Column(db.Text)
    mimetype = db.Column(db.Text, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)