from flask import Flask, request, jsonify, json
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'HEy!! Pass data to be encrypted'


@app.route('/encrypt', methods=['GET'])
def get_symbol_data():
    print("$$$$$$$$$$$$$$$$$$$$$$$")
    # data = request.json
    # print(data)
    return jsonify({"gopal":"yadav"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')