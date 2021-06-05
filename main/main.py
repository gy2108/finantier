from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from Finantier :)'


@app.route('/symbol/<string:symbol>', methods=['GET'])
def get_symbol_data(symbol):
    # resp = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=7KK8XVZ5Y2AF0ZL6".format(symbol))
    # r = resp.json()
    # data_points_dict = {}
    # for key, value in r["Global Quote"].items():
    #     data_points_dict[key.split(" ")[1]] = value
    
    r = requests.get("https://localhost:5000/encrypt")
    print(r.text)
    print(r.status_code)
    return r
    # return jsonify(data_points_dict)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')