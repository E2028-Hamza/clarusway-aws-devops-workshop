from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        user_input = request.form["number"]
        if user_input.isalpha() or user_input == "0":
            return render_template("index.html", developer_name = "Hamza Seyyah", not_valid= True)
        else:
            user_input = int(user_input)
        if user_input < 1 :
            return render_template("index.html", developer_name = "Hamza Seyyah", not_valid= True)
        else:
            def convert(milliseconds):
                result = ''
                milliseconds = user_input
                hour_in_milliseconds = 60*60*1000
                hours = milliseconds // hour_in_milliseconds
                milliseconds_left = milliseconds % hour_in_milliseconds
                minutes_in_milliseconds = 60*1000
                minutes = milliseconds_left // minutes_in_milliseconds
                milliseconds_left %= minutes_in_milliseconds
                seconds = milliseconds_left // 1000
            return f'{hours} hour/s'*(hours != 0) + f' {minutes} minute/s'*(minutes != 0) + f' {seconds} second/s' *(seconds != 0) or f'just {milliseconds} millisecond/s' * (milliseconds < 1000)
        return render_template("result.html", developer_name = "Hamza Seyyah", number_decimal = number_decimal, number_roman=number_roman)
    else:
        return render_template("index.html", developer_name = "Hamza Seyyah")

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)
