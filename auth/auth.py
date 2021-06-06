from flask import Flask, jsonify, make_response
import requests
import jwt
import datetime

app = Flask(__name__)

app.config['SECRET_KEY']='finantiersecretkey'

@app.route('/')
def home():
    return 'Auth Service !!!'


@app.route('/token/<int:user_id>', methods=['GET'])
def get_symbol_data(user_id):
    if not user_id:
        return make_response(
            jsonify({"error_message": "Please provide user id"}), 400)
    token = jwt.encode({'user_id': user_id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=30)},
                        app.config['SECRET_KEY'])  
    return jsonify({'token' : token})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')