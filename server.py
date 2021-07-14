from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello_word():
    return 'Hello, World!'


@app.route('/summa', methods=['GET'])
def summa():
    data = request.args
    product = int(data["x"]) + int(data["y"])
    return str(product)


@app.route('/division', methods=['POST'])
def division():
    data = request.json
    portion = int(data["a"]) // int(data["b"])
    return str(portion)
