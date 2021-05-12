from flask import Blueprint, render_template, jsonify, request
import json
from classes.komay_class import Song

ks = Blueprint('ks', __name__ , url_prefix='/ks', static_folder="static", template_folder="templates/ks/")

@ks.route('/')
def index():
    if(request.method == 'POST'):
        artist = request.form.get('artist')
        song = request.form.get('song')
        sort_method = request.form.get('sorttype')

        return render_template('getsongs.html', song = Song(artist, song, 'similarity'), background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg")

    return render_template('getsongs.html', background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg", song = Song('Queen', "Bohemian+Rhapsody", "similarity"))
@ks.route('/')
def bubbleSort():
    if(request.method == 'POST'):
        artist = request.form.get('artist')
        song = request.form.get('song')
        sort_method = request.form.get('sorttype')

        return render_template('getsongs.html', song = Song(artist, song, sort_method), background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg")

    return render_template('getsongs.html', background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg", song = Song('Queen', "Bohemian+Rhapsody", "similarity"))