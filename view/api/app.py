from flask import Blueprint, render_template, jsonify, request, url_for
import json, random
with open('backgrounds.json') as file:
    backgroundJSON = json.load(file)
    bg = backgroundJSON['backgrounds']

api = Blueprint('api', __name__ ,url_prefix='/api', static_folder="static", template_folder="templates")
from model import Playlist


@api.route('/')
def index():
    endpoints = {
        url_for('api.all'): "Returns all user submitted playlist objects in the database",
        url_for('api.randomPlaylist'): "Returns a random user submitted playlist object from the database",
        "/api/playlists/{INTEGER}": "Returns a user submitted playlist object by ID from the database",
        url_for('api.randomBackground'): "Returns a random url of one of the backgrounds used on the site"
    }
    return(jsonify(endpoints))

@api.route('/playlists/all', methods = ["GET","POST"])
def all():
    all_playlists = Playlist.query.all()
    playlists = []

    for item in all_playlists:
       

        appenditem = {
            'id': item.id,
            'playlistname': item.playlistname,
            'username': item.username,
            'url': item.url,
        }
        playlists.append(appenditem)
    return jsonify(playlists)
@api.route('/playlists/random', methods = ["GET","POST"])
def randomPlaylist():
    all = Playlist.query.all()
    playlists = []

    for item in all:
        appenditem = {
            'id': item.id,
            'playlistname': item.playlistname,
            'username': item.username,
            'url': item.url,
        }
        playlists.append(appenditem)

    return jsonify(random.choice(playlists))

@api.route('/playlists/<int:id>')
def get_playlist(id):
    playlist = Playlist.query.filter_by(id=id).first()
    if playlist:
        playlist_dict = {
            'id': playlist.id,
            'username': playlist.username,
            'playlist_name': playlist.playlistname,
            'playlist_url': playlist.url,

        }
        return jsonify(playlist_dict)

    else:
        return Response("No playlist with that id ", status=400)


@api.route('/backgrounds/random', methods = ["GET","POST"])
def randomBackground():

    return jsonify({'url': random.choice(bg)})
