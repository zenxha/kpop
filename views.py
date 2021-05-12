"""Views in MVC has responsibility for establishing routes and rendering HTML"""

import random
import requests
import json
from flask import g, jsonify
from flask import render_template, request, redirect, url_for, session, Flask, Response

from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from BlueprintsIndividual.sample_bp import kpop, jpop
from BlueprintsIndividual.api_view import api
from BlueprintsIndividual.charlie import cz
from BlueprintsIndividual.komay import ks
from views.chris.app import chris_bp
from BlueprintsIndividual.devam import ds
from BlueprintsIndividual.eshaan import ep
#from db import db_init, db
#from model import Review, User
with open('config.json') as file:
    config = json.load(file)


app = Flask(__name__)
app.register_blueprint(kpop, url_prefix="/kpop")
app.register_blueprint(jpop, url_prefix="/jpop")
app.register_blueprint(api)
app.register_blueprint(cz)
app.register_blueprint(ks)
app.register_blueprint(chris_bp, url_prefix='/cr')
app.register_blueprint(ds)
app.register_blueprint(ep)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db_init(app)

db = SQLAlchemy()

backgrounds = ["https://www.teahub.io/photos/full/193-1933361_laptop-aesthetic-wallpapers-anime.jpg"]

pathForImages='./images/'
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/')
def index():
    #response = requests.get('https://nekos.life/api/v2/img/wallpaper')
    #background = response.json()['url']
    response = requests.get('https://api.quotable.io/random?maxLength=60')
    quote = response.json()['content']
    author = response.json()['author']
    background = random.choice(backgrounds)
    return render_template("index.html", background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg", quote=quote, author = author)

@app.route('/bootstrap')
def bootstrap_sample():
    return render_template("Bootstrap_login_example.html")


"""our own project dstufsuf as"""

@app.route('/project')
def project():
    return render_template("homesite/project.html", background=random.choice(backgrounds))
@app.route('/easteregg')
def easteregg():
    return render_template("easteregg/base.html", background="https://i.pinimg.com/originals/b8/e2/70/b8e270b7237f2f4c3a5905e6a3ca5f63.png")

@app.route('/browse')
def browse():
    backgrounds = ["https://cdn.discordapp.com/attachments/784178874303905792/818606015494094868/812382.png"]
    review_query = Review.query.all()
    reviews = []

    for review in review_query:
        websiteurl = url_for('get_img', id=review.id)

        review_dict = {
            'id': review.id,
            'username': review.username,
            'content': review.content,
            'satisfaction': review.satisfaction,
            'image':  websiteurl
        }
        reviews.append(review_dict)
    return render_template("homesite/browse.html", reviews=reviews, background=random.choice(backgrounds))

@app.route('/easteregg/crossover')
def crossover():
    return render_template("easteregg/crossover.html")

@app.route('/upload', methods=["POST", 'GET'])
def upload():
    background = random.choice(backgrounds)
    if request.method == "POST":
        name = request.form["username"]
        satisfaction = request.form["satisfaction"]
        content = request.form["content"]
        image = request.files.get('img')
        if not image:
            return 'bad news ur image didnt make it to our servers :((((', 400

        filename = secure_filename(image.filename)
        mimetype = image.mimetype
        if not filename or not mimetype:
            return 'Bad upload', 400

        review = Review(username=name, content=content, img=image.read(), filename=filename, satisfaction=satisfaction,mimetype=mimetype)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("browse"))
    return render_template("homesite/loginv2.html", background=background)

@app.route('/images/<int:id>')
def get_img(id):
    img = Review.query.filter_by(id=id).first()
    if not img:
        return 'No img with that id', 200

    return Response(img.img, mimetype=img.mimetype)


"Login Section"


@app.route('/login', methods=["POST", "GET"])
def login_post():
    if request.method == "POST":
        password = request.form.get('password')
        name = request.form.get("username")
        user = User.query.filter_by(username=name).first()
        if name == "mort":
            return render_template('easteregg/IAM.html')
        if not user: return render_template('signup.html', error="Please sign up for an account first")
        if user.password == password:
            session.pop('user', None)
            session['user'] = user.username
            return redirect(url_for('upload'))
        else:
            return render_template('homesite/login.html', error="Please check your credentials and try again", background = random.choice(backgrounds))

    return render_template("homesite/login.html", background = random.choice(backgrounds))


"""
@app.route('/profile/<int:id>')
def profile(id):
    img = 2
    return render_template("homesite/profile.html", name=current_user.name)
"""


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if name == "mort": # easter egg
            return render_template('easteregg/IAM.html')

        user = User.query.filter_by(username=name).first() # if this returns a user, then the email already exists in database

        if user:  # if a user is found, we want to redirect back to signup page so user can try again
            return "choose a new username"
        else:
            # create a new user with the form data. Hash the password so the plaintext version isn't saved.
            new_user = User(username=name, password=password, email=email)

            # add the new user to the database
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for("login_post"))
    return render_template('signup.html', background = random.choice(backgrounds))


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("index"))

