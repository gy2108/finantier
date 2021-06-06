from flask import Flask, jsonify, make_response
import requests

app = Flask(__name__)


ENCRYPT_SERVICE_URL = "http://encrypt_service:5000/encrypt"

@app.route('/')
def home():
    return 'Hello from Finantier :)'


@app.route('/symbol/<string:symbol>', methods=['GET'])
def get_symbol_data(symbol):

    stock_resp = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=7KK8XVZ5Y2AF0ZL6".format(symbol))

    stock_data = stock_resp.json()
    if "Global Quote" not in stock_data:
        return make_response(
            jsonify({"error_message": "Please try after Some time"}), 500)

    data_points_dict = {}
    for key, value in stock_data["Global Quote"].items():
        data_points_dict[key.split(" ")[1]] = value

    encrypt_resp = requests.get(url=ENCRYPT_SERVICE_URL, json=data_points_dict)
    if encrypt_resp.status_code == 200:
        return make_response(jsonify(encrypt_resp.json(), 200))
    else:
        return make_response(jsonify({"error_message": "Please try after some time"}), 500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')