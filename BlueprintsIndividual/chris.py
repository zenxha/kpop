from flask import Blueprint, render_template, request
from classes.chris_class import song, BubbleSort


cr = Blueprint('cr', __name__, url_prefix="/cr", static_folder="static", template_folder="templates")

@cr.route('/')
@cr.route('/home')
def index():
    songs = [{
            "title": "Party Rock Anthem",
            "link": "https://www.youtube.com/embed/KQ6zr6kCPj8",
            },
            {
            "title": "Uptown Funk",
            "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
            },
            {
            "title": "Wrecking Ball",
            "link": "https://www.youtube.com/embed/My2FRPA3Gf8",
            },
            {
            "title": "A Thousand Miles",
            "link": "https://www.youtube.com/embed/Cwkej79U3ek",
            }]
    return render_template('shuffle.html', song=song(songs), songarray=songs)

@cr.route('/bubble', methods = ["GET","POST"])
def bubbleSort():
    arr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        arr = string.split()
        original = string.split()
        if(request.form["select"] == "integer"):
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(original)):
                    original[j] = int(original[j])
                return render_template("crbubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("crbubblesort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
        else:
            try:
                isString = True
                return render_template("crbubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = original)
            except ValueError:
                return render_template("crbubblesort.html",output_list = "Can Only Contain String or Integer",original_list = "Error")
    return render_template("crbubblesort.html",output_list = BubbleSort(arr,isString).OuputList,original_list = arr)