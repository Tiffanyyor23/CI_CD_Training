#!/usr/bin/env python3

from flask import Flask, request
from calculator import Calculator

app = Flask(__name__)

@app.route("/")
def math():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = Calculator(a,b)
    return str(answer)
   


if __name__ == "__main__":
    app.run(host='0.0.0.0')

