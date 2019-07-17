#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import choice
import string
app = Flask(__name__)

@app.route(methods=['GET'])
def text_gen_lower():
    rand = random.choice(string.ascii_lowercase) for x in (3)
    return jsonify({"Random Characters":rand})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
