#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import randint
app = Flask(__name__)


@app.route('/getNums', methods=['GET'])
def num_gen_8():
    randcollector = ''
    for x in range(8):
        rand = randint(0, 9)
        randcollector += str(rand)
    return randcollector

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9018)
