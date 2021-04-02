from flask import Blueprint, render_template, jsonify, request
import json
from classes.class_test import Song

ks = Blueprint('ks', __name__ ,url_prefix='/komay', static_folder="static", template_folder="templates")

@ks.route('/')
def index():
    song = Song('official hige dandism', 'pretender').get_similar()
    return song
@ks.route('/getsong', methods=["POST", 'GET'])
def getsong():
    if(request.method == 'POST'):
        artist = request.form.get('artist')
        song = request.form.get('song')
        return render_template('getsongs.html', background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg", song = Song(artist, song))

    return render_template('getsongs.html', background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg", song = Song('Official+HIGE+DANdism', "pretender"))