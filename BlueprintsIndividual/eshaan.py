from flask import Blueprint, Flask, render_template, jsonify, request
from classes.eshaan_class import top_5, EshaanBubbleSort

ep = Blueprint('ep', __name__, url_prefix="/eshaan", static_folder="static", template_folder="templates")

@ep.route('/top5')
def index():
    tracks = [{
            "title": "Mirrors by Jason Richardson",
            "link": "https://www.youtube.com/embed/Utj1VuJE7V0",
            "description": "Very-fast paced metal with no vocals and a heavy guitar focus. Not for everyone but my personal favorite."

        },
        {
            "title": "A Cruel Angel's Thesis",
            "link": "https://www.youtube.com/embed/k8ozVkIkr-g",
            "description": "Renowned as the opening track from 'Neon Genesis Evangelion,' this one is reminiscent of a casual jam session close friends would have."
        },
        {
            "title": "505 by Arctic Monkeys",
            "link": "https://www.youtube.com/embed/MrmPDUvKyLs",
            "description": "An oldie but goodie, it's very much a vibe of walking downtown during midnight."
        },
        {
            "title": "More Than A Woman by The Bee Gees",
            "link": "https://www.youtube.com/embed/zwyKQnbDJRg",
            "description": "From the film 'Saturday Night Fever,' this song will surely get your body wiggling onto the dance floor at any time."
        },
        {
            "title": "Billie Jean by Michael Jackson",
            "link": "https://www.youtube.com/embed/Zi_XLOBDo_Y",
            "description": "If you don't know this classic, then you are missing out!"
        }]
    return render_template('recommend.html', track=top_5(tracks), trackarray=tracks)

@ep.route('/bubble', methods = ["GET", "POST"])
def bubbleSort():
    inarr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        inarr = string.split()
        input = string.split()
        if(request.form["select"] == "string"):
            try:
                isString = True
                return render_template("crbubblesort.html",sorted_list = EshaanBubbleSort(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        else:
            try:
                for j in range (0,len(inarr)):
                    inarr[j] = int(inarr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("crbubblesort.html",sorted_list = EshaanBubbleSort(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("crbubblesort.html",sorted_list = EshaanBubbleSort(inarr,isString).OutputList,input_list = inarr)
