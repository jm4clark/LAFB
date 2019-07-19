#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
import random
import string
app = Flask(__name__)

@app.route('/getText', methods=['GET'])
def text_gen_upper():
    randcollector = ''
    for x in range (0, 2):
        rand = random.choice(string.ascii_uppercase)
        randcollector += rand
    return randcollector


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9019)
