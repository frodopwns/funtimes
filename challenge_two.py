import csv
import codecs
from flask import Flask, jsonify

app = Flask(__name__)
locations = {}
blocks = []

@app.route("/<ip>")
def index(ip):
    ip = int("".join(ip.split(".")))
    _id = None

    _index = binary_search(blocks, ip)
    if _index > -1:
        _id = blocks[_index][2]
        return jsonify(**locations[_id])
    else:
        return "fail"

def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if seq[m][0] < t:
            min = m + 1
            if t <= seq[m][1] and t >= seq[m][0]:
                return m
        elif seq[m][0] > t:
            max = m - 1
            if t <= seq[m][1] and t >= seq[m][0]:
                return m
        else:
            return m

def parse_data():

    filehandler = codecs.open("GeoLiteCity-Blocks.csv", 'rU')
    f = csv.reader(filehandler)
    for i, row in enumerate(f):
        if i < 2:
            pass
        else:
            blocks.append(map(int, row))

    filehandler = codecs.open("GeoLiteCity-Location.csv", 'rU')
    f = csv.reader(filehandler)
    for i, row in enumerate(f):
        if i == 1:
            header = list(row)
        elif i < 2:
            pass
        else:
            locations[int(row[0])] = dict(zip(header, row))


if __name__ == '__main__':
    parse_data()
    #Create an Instance of Flask
    app.debug = True
    app.run()












