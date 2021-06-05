from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello from Finantier :)'


@app.route('/symbol/<str:symbol>', methods=['GET'])
def get_symbol_data(symbol):
    r = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=demo".format(symbol))
    return r.json()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')