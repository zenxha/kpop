from flask import Blueprint, render_template, jsonify, request
from classes.charlie_class import game, CharlieBubbleSort
import json
with open('config.json') as file:
    config = json.load(file)

cz = Blueprint('cz', __name__, url_prefix="/cz", static_folder="static", template_folder="templates")

@cz.route('/')
def index():
    gamesDict = [{
        "title": "ARK: Survival Evolved",
        "releasedate": "2015-06-02",
        "randomfact": "The game was designed by Kayd Hendricks.",

    },
        {
            "title": "Risk of Rain 2",
            "releasedate": "2019-03-28",
            "randomfact": "It's a roguelike third-person shooter developed by Hopoo Games",
        },
        {
            "title": "The Binding of Isaac",
            "releasedate": "2011-09-28",
            "randomfact": "The game was the result of a week-long game jam between McMillen and Himsl to develop a The Legend of Zelda-inspired roguelike",
        },
        {
            "title": "Minecraft",
            "releasedate": "2011-11-18",
            "randomfact": "The game was created by Markus Notch",
        }]
    games = []
    for i in gamesDict:
        games.append(game(i['title'], i['releasedate'], i['randomfact']))
    return render_template('games.html', gamelist=games)

@cz.route('/bubble', methods = ["GET","POST"])
def bubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        input = string.split()
        if(request.form["select"] == "string"):
            try:
                isString = True
                return render_template("czbubblesort.html",sorted_list = CharlieBubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("czbubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        else:
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("czbubblesort.html",sorted_list = CharlieBubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("czbubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("czbubblesort.html",sorted_list = CharlieBubbleSort(arr,isString).OutputList,input_list = arr)