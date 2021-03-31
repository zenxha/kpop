from flask import Blueprint, render_template, jsonify
import json
from classes.class_test import Song

ks = Blueprint('ks', __name__ ,url_prefix='/komay', static_folder="static", template_folder="templates")

@ks.route('/')
def index():
    song = Song('official hige dandism', 'pretender').get_similar()
    return song.get_similar()