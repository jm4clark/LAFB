#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import choice
import string
app = Flask(__name__)

randcollector = ""

@app.route(methods=['GET'])
def text_gen_lower():
    for x in range (0, 2):
        rand = random.choice(string.ascii_uppercase)
        randcollector += rand
        return jsonify({"Random Characters":randcollector})


@app.route(methods=['GET'])
def text_gen_upper():
    rand = random.choice(string.ascii_uppercase) for x in (2)
    return jsonify({"Random Characters":rand})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
