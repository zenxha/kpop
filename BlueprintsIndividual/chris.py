from flask import Blueprint, render_template
from classes.chris_class import song


cr = Blueprint('cr', __name__, url_prefix="/cr", static_folder="static", template_folder="templates")

@cr.route('/')
@cr.route('/home')
def index():
    songs = [{
            "title": "Party Rock Anthem",
            "link": "https://www.youtube.com/embed/KQ6zr6kCPj8",
            "description":"LITERALLY EVERYONE LOVES THIS SONG"
        },
        {
            "title": "Uptown Funk",
            "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
            "description":"Some people like this song"
        },
        {
            "title": "Wrecking Ball",
            "link": "https://www.youtube.com/embed/My2FRPA3Gf8",
            "description":"nobody likes this song"
        },
        {
            "title": "A Thousand Miles",
            "link": "https://www.youtube.com/embed/Cwkej79U3ek",
            "description":"This song is just really catchy"
        }]
    return render_template('shuffle.html', song=song(songs), songarray=songs)