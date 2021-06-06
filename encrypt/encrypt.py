from flask import Flask, request, jsonify, json, make_response
import requests
import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

app = Flask(__name__)


@app.route('/')
def home():
    return 'Encrypt Service !!! Use "/encrypt" endpoint  to encrypt your data'

class AESCipher(object):
    def __init__(self, key): 
        #Can store this key in some other central repository
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


@app.route('/encrypt', methods=['GET'])
def get_encrypt_symbol_data():
    data = request.json
    cipher_obj = AESCipher(key="mysecretpassword")
    cipher_byte = cipher_obj.encrypt(str(data))
    cipher_text = cipher_byte.decode("utf-8")
    # cipher_text = bytes(cipher_text, 'utf-8')
    # print(cipher_obj.decrypt(str(cipher_text)))
    return make_response(jsonify({"cipher_text": cipher_text}), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')