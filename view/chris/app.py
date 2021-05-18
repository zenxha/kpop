from flask import Blueprint, render_template, request
from .algo.songshuffle import song
from .algo.bubblesort import BubbleSort


chris_bp = Blueprint('chris_bp', __name__, template_folder='templates', static_folder='static', static_url_path='assets')


@chris_bp.route('/')
def index():
    return render_template('chrishome.html')


@chris_bp.route('/shuffle')
def shuffle():
    return render_template('shuffle.html', song=song())


@chris_bp.route('/bubble', methods = ["GET","POST"])
def bubbleSort():
    inarr = []
    isString = False
    if request.form:
        string = request.form.get("string")
        inarr = string.split()
        input = string.split()
        # check if inputted values are string
        if(request.form["select"] == "string"):
            #if string then sort strings
            try:
                isString = True
                return render_template("crbubblesort.html",sorted_list = BubbleSort(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        #if not string then sort for integers
        else:
            try:
                for j in range (0,len(inarr)):
                    inarr[j] = int(inarr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("crbubblesort.html",sorted_list = BubbleSort(inarr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("crbubblesort.html",sorted_list = BubbleSort(inarr,isString).OutputList,input_list = inarr)