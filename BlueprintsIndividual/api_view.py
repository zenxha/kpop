
# Komay's API blueprint
from flask import Blueprint, render_template, jsonify
import json
with open('config.json') as file:
    config = json.load(file)

api = Blueprint('api', __name__, url_prefix="/api", static_folder="static", template_folder="templates")

@api.route('/')
def index():
    return "Current endpoints: <br><br>"+ config['websiteURL'] + "/api/review/id={ID}  - Returns a review object with the same id<br><br>" + config['websiteURL'] + "/api/review/all  - Returns all reviews stored on the server. "

@api.route('/songs/<string:name>')
def get_review(name):

        song = {
            'name': name,
            'song for you ': "Pretender",
            'url': "https://www.youtube.com/watch?v=TQ8WlA2GXbk",
        }
        return jsonify(song)



@api.route('/songs/all')
def get_all_reviews():

    return jsonify("your mom this isnt finished lmao")
@api.route('/songs/')
def allsongs():

    return jsonify("your mom this isnt finished lmao")