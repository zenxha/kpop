from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Function that initializes the db and creates the tables
def db_init(app):
    db.init_app(app)

    # Creates the logs tables if the db doesnt already exist
    with app.app_context():
        db.create_all()
        print('h')

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlistname = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)

class MV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songname = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False)