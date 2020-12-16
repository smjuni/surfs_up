from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

def name():
    name = [Stephanie]
    return f"{hello_world}, my name is (str{name})"
