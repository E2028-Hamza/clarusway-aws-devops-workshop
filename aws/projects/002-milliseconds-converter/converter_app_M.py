from flask import Flask, render_template, request
from converter import conv_mil

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    num = request.form.get("number")

    if request.method == "POST" and ((not num.isdigit()) or  (int(num) < 1)):
        return render_template("index.html", developer_name = "Muhammet P.", not_valid = True)

    elif request.method == "POST":
        return render_template("result.html", milliseconds = num, result = conv_mil(num),  developer_name = "Muhammet P.")

    else:
        return render_template("index.html", developer_name = "Muhammet P.")

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)