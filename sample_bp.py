from flask import Blueprint
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response, Blueprint
bp = Blueprint('bp', __name__)
bp2 = Blueprint('bp2', __name__)

@bp.route('/')
def index():
    return "I love K-Pop!"

@bp.route('/base')
def purpose():
    return render_template("base.html")

@bp2.route('/')
def index2():
    return "I love J-Pop!"

@bp2.route('/base')
def purpose2():
    return render_template("base.html")

