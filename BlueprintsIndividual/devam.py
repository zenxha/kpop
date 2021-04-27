from flask import Blueprint, render_template, jsonify, request
import json
# from classes.komay_class import Video, Song

ds = Blueprint('ds', __name__, url_prefix='/devam', static_folder="static", template_folder="templates")


@ds.route('/')
def index():
    video = Video('Music Videos', 'idk').get_similar()
    return video


@ds.route('/musicvids', methods=["POST", 'GET'])
def musicvids():
    if (request.method == 'POST'):
        creator = request.form.get('creator')
        vidname = request.form.get('vidname')
        return render_template('getMV.html', video=Video(creator, vidname))
    return render_template('getsongs.html', background="https://cdn.wallpapersafari.com/91/31/z4AvR6.jpg",
                           song=Song('Official+HIGE+DANdism', "pretender"))
