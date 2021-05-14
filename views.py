"""Views in MVC has responsibility for establishing routes and rendering HTML"""
import os
import random
import requests
import json
from flask import g, jsonify, flash
from flask import render_template, request, redirect, url_for, session, Flask, Response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField , IntegerField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from BlueprintsIndividual.sample_bp import kpop, jpop
from BlueprintsIndividual.api_view import api
from BlueprintsIndividual.charlie import cz
from view.komay.app import ks
from view.chris.app import chris_bp
from BlueprintsIndividual.devam import ds
from BlueprintsIndividual.eshaan import ep
#from db import db_init, db
#from model import Review, User
with open('config.json') as file:
    config = json.load(file)


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login_route'
app.register_blueprint(kpop, url_prefix="/kpop")
app.register_blueprint(jpop, url_prefix="/jpop")
app.register_blueprint(api)
app.register_blueprint(cz)
app.register_blueprint(ks)
app.register_blueprint(chris_bp, url_prefix='/cr')
app.register_blueprint(ds)
app.register_blueprint(ep)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
dbURI = 'sqlite:///' + os.path.join(basedir, 'models/myDB.db')
""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = "qwerty"
db = SQLAlchemy(app)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordconfirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo("password")])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
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
def bootstrap():
    return render_template('Bootstrap_login_example.html')


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


@app.route('/signin', methods=["POST", "GET"])
def login_route():
    logform = LoginForm()
    if logform.validate_on_submit():
        user = User.query.filter_by(username=logform.username.data).first()
        if user is None or not user.check_password(logform.password.data):
            flash("Login Failed")
            return redirect("/signin")
        login_user(user)
        flash("Login Successful!")
        if logform.username.data == "secret":
            return redirect("/secret")
        nextpage = request.args.get("next")
        if not nextpage or url_parse(nextpage).netloc != '':
            return redirect('/')
        return redirect(nextpage)
    else:
        return render_template("signin.html", form = logform)


"""
@app.route('/profile/<int:id>')
def profile(id):
    img = 2
    return render_template("homesite/profile.html", name=current_user.name)
"""
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
    regform = RegisterForm()
    """Register user"""
    if regform.validate_on_submit():
        newUser = User(username=regform.username.data, first_name=regform.firstname.data, last_name=regform.lastname.data, email=regform.email.data)
        newUser.set_password(regform.password.data)
        # Insert all the values into the database
        db.session.add(newUser)
        db.session.commit()
        return redirect("/signin")
    else:
        return render_template("signup.html", form = regform)

@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == "POST":
        newuser = request.form["newusername"] # using name as dictionary key
        # redirects us to the user page
        return redirect(url_for("newuser", newusr=newuser))
    else:
        return render_template("signin.html")

@app.route('/database')
@login_required
def index2():
    data = User.query.all()
    return render_template('database.html', data=data)

@app.route("/<usr>")
def user(usr):
    return "<h1>"+usr+"</h1>"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for("index"))

