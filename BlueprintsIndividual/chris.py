from flask import Blueprint, render_template, request
from classes.chris_class import song, BubbleSort


cr = Blueprint('cr', __name__, url_prefix="/cr", static_folder="static", template_folder="templates")


@cr.route('/shuffle')
def shuffle():
    return render_template('shuffle.html', song=song())


@cr.route('/bubble', methods = ["GET","POST"])
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
                return render_template("crbubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain A String",input_list = "Error")
        else:
            try:
                for j in range (0,len(arr)):
                    arr[j] = int(arr[j])
                for j in range (0,len(input)):
                    input[j] = int(input[j])
                return render_template("crbubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = input)
            except ValueError:
                return render_template("crbubblesort.html",sorted_list = "Can Only Contain An Integer",input_list = "Error")

    return render_template("crbubblesort.html",sorted_list = BubbleSort(arr,isString).OutputList,input_list = arr)