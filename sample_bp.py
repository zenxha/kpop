from flask import Blueprint
from flask import render_template, request, redirect, url_for, session, flash, Flask, Response, Blueprint
bp = Blueprint('example_blueprint', __name__)

@bp.route('/')
def index():
    return "Hello World!"

@bp.route('/base')
def purpose():
    return render_template("base.html")