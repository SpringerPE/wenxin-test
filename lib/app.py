from flask import Flask

app = Flask(__name__)

@app.route("/test")
def hello():
    return "Hello World!"

@app.route("/")
def hello1():
    return "Hi"


