from flask import Blueprint, render_template, jsonify
from classes.charlie_class import games
import json
with open('config.json') as file:
    config = json.load(file)

cz = Blueprint('cz', __name__, url_prefix="/cz", static_folder="static", template_folder="templates")

@cz.route('/')
def index():
    return render_template('fibonacci.html', gamelist=games([]))