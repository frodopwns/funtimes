import csv
import codecs
from flask import Flask, jsonify

app = Flask(__name__)
locations = {}
blocks = []

@app.route("/<ip>")
def index(ip):
    """
    Handles /ip where ip is an address in the form
    ddd.ddd.d.d (eg 123.123.1.1)
    """
    ip = int("".join(ip.split(".")))
    _id = None

    _index = binary_search(blocks, ip)
    if _index > -1:
        _id = blocks[_index][2]
        return jsonify(**locations[_id])
    else:
        return "not found"

def binary_search(seq, t):
    """
    Binary search search for blocks list
    """
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
    """
    Open the csvs and read them into memory
    """
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












