from flask import Flask, request, render_template, json, redirect, url_for, Blueprint
import json
import os.path

app = Flask(__name__)
app.secret_key = 'sadjkfhaslehr'

@app.route("/", methods=["POST", "GET"])
def home():
    with open('text_chooser.json', 'r') as f:
        word = json.loads(f.read())

    if request.method == "GET":

        fileObject = open("data/choices.json", "r")
        jsonContent = fileObject.read()
        choose = json.loads(jsonContent)

        return render_template("index.html", choose=choose)

@app.route("/data", methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        text_chooser = request.form['chosen']
        with open('text_chooser.json', 'w') as text_file:
            json.dump(text_chooser, text_file)
        return render_template("data.html", chosen = request.form['chosen'])
    else:
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = "5000")
