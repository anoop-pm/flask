import re
from itertools import count

from flask_cors import CORS
from flask_cors import cross_origin

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/Exam", methods=["GET", "POST"])
def Exam():

    file = request.json

    result = file["file"]
    new = file["lfrom"]
    li = file["limit"]
    print("li")

    a_file = open(result)
    lists = []
    lines = a_file.readlines()
    for i in range(new, li):
        lists.append(lines[i])

    print(lists)
    return {"result": lists}


if __name__ == "__main__":

    app.run(debug=True)
