from flask import Blueprint
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response, Blueprint
kpop = Blueprint('kpop', __name__)
jpop = Blueprint('jpop', __name__)

@kpop.route('/')
def index():
    return "I love K-Pop!"

@kpop.route('/base')
def purpose():
    return render_template("base2.html")

@jpop.route('/')
def index2():
    return "I love J-Pop!"

@jpop.route('/base')
def purpose2():
    return render_template("base2.html")

