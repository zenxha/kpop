from flask import Blueprint, render_template, jsonify, request
import json, random


api = Blueprint('api', __name__ ,url_prefix='/api', static_folder="static", template_folder="templates")
from model import Playlist
@api.route('/all', methods = ["GET","POST"])
def index():
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
    return jsonify(playlists)
@api.route('/random', methods = ["GET","POST"])
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

    