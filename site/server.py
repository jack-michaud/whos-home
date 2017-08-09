import csv
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    context = {}
    return render_template('index.html', **context)

@app.route("/data")
def fetch_data():
    csvfile = open('logs.csv', 'rb')
    reader = csv.reader(csvfile, delimiter=',')
    context = []
    for row in reader:
        context.append({"date": row[0], "hostname": row[1], "ip": row[2], "mac": row[3]})

    csvfile.close()
    return jsonify(context)



