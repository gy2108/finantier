from flask import Flask, jsonify, make_response, request
import requests
from functools import wraps
import jwt

app = Flask(__name__)


ENCRYPT_SERVICE_URL = "http://encrypt_service:5000/encrypt"
app.config['SECRET_KEY'] = 'finantiersecretkey'


@app.route('/')
def home():
    return 'Hello from Finantier :)'


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return jsonify({'message': 'a valid token is missing'})
        try:
            data = jwt.decode(token.split(" ")[1], app.config['SECRET_KEY'], algorithms='HS256')
        except Exception as e:
            print(e)
            return jsonify({'message': 'token is invalid'})

        return f(*args, **kwargs)
    return decorator


@app.route('/symbol/<string:symbol>', methods=['GET'])
@token_required
def get_symbol_data(symbol):

    stock_resp = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=7KK8XVZ5Y2AF0ZL6".format(symbol))

    stock_data = stock_resp.json()
    if "Global Quote" not in stock_data:
        return make_response(
            jsonify({"error_message": "Please try after Some time"}), 500)

    if not stock_data["Global Quote"]:
        return make_response(
            jsonify({"error_message": "Not a Valid Symbol"}), 404)

    data_points_dict = {}
    for key, value in stock_data["Global Quote"].items():
        data_points_dict[key.split(" ")[1]] = value

    token = request.headers['Authorization']
    encrypt_resp = requests.get(url=ENCRYPT_SERVICE_URL, json=data_points_dict, headers={'Authorization': '{}'.format(token)})
    if encrypt_resp.status_code == 200:
        return make_response(jsonify(encrypt_resp.json()), 200)
    else:
        return make_response(jsonify({"error_message": "Please try after some time"}), 500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')