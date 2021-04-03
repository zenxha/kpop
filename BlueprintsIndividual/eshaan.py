from flask import Blueprint, Flask, render_template, json
from classes.eshaan_class import eshaan_top_5

ep = Blueprint('ep', __name__, url_prefix="/eshaan", static_folder="static", template_folder="templates")

@ep.route('/')
def index():
    top_5_tracks = [{
            "title": "Mirrors By Jason Richardson",
            "link": "https://www.youtube.com/embed/Utj1VuJE7V0",
            "description": "Very fast-paced metal is the best way to describe it. Not liked by everyone, but definitely my style."
        },
        {
            "title": "A Cruel Angel's Thesis by Shiro Sagisu",
            "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
            "description": "Originated from the famous anime 'Neon Genesis Evangelion,' it's quite reminiscint of a casual jam session."
        },
        {
            "title": "505 by Arctic Monkeys",
            "link": "https://www.youtube.com/embed/MrmPDUvKyLs",
            "description": "An oldie but goodie, it reminds me of walking through the streets in downtowwn LA."
        },
        {
            "title": "More Than A Woman by The Bee Gees",
            "link": "https://www.youtube.com/embed/zwyKQnbDJRg",
            "description": "An old classic from 'Saturday Night Fever,' it's very good at getting listeners onto their feet and moving on the dance floor!"
        },
        {
            "title": "Billie Jean by Michael Jackson",
            "link": "https://www.youtube.com/embed/Zi_XLOBDo_Y",
            "description": "Everyone knows this song, and if you don't, I'm going to assume you live under a rock."
        }]
    return render_template('recommend.html', top_5=eshaan_top_5(top_5_tracks), top_5_array = top_5_tracks)