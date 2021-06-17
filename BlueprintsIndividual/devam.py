from flask import Blueprint, render_template, jsonify, request
import json
from classes.charlie_class import game, CharlieBubbleSort
# from classes.komay_class import Video, Song

ds = Blueprint('ds', __name__, url_prefix='/devam', static_folder="static", template_folder="templates")


@ds.route('/')
def index():
    video = Video('Music Videos', 'idk').get_similar()
    return video


@ds.route('/bubble', methods = ["GET","POST"])
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
                return render_template("czbubblesort.html",sorted_list = BubbleSortDevam(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("czbubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        else:
            try:
                for j in range (0,len(inarr)):
                    inarr[j] = int(inarr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("czbubblesort.html",sorted_list = CharlieBubbleSort(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("czbubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("czbubblesort.html",sorted_list = CharlieBubbleSort(inarr,isString).OutputList,input_list = inarr)