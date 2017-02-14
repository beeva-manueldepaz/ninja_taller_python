from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/hello")
def hello_json():
    return jsonify(dict(message="Hello from python"))

@app.route("/sum")
def suma():
    num_1 = request.args.get("num1", 0)
    num_2 = request.args.get("num2", 0)
    # result = str(num_1) + str(num_2)
    result = int(num_1) + int(num_2)
    return jsonify(dict(sum=result))

app.run(host="127.0.0.1")
