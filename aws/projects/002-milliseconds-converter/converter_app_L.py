from flask import Flask, render_template, request

from millisecond_func_L import *

converter_app = Flask(__name__)

@converter_app.route("/", methods = ["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html", developer_name = "Charlie Falcon")

@converter_app.route("/", methods = ["POST"])
def check_do():
    if request.method == "POST":    
        user_input = request.form["number"]

        if isValid(user_input) == False:
            return render_template("index.html", developer_name = "Charlie Falcon", not_valid= True)
        
        else:    
            return render_template("result.html", developer_name = "Charlie Falcon", milliseconds = user_input, result = doCalc(user_input))

if __name__ == '__main__':
    converter_app.run(debug = True)
    #converter_app.run(host='0.0.0.0', port=80)