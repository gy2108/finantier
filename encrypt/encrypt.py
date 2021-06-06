from flask import Flask, request, jsonify, json
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Encrypt Service !!!'


@app.route('/encrypt', methods=['GET'])
def get_symbol_data():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')