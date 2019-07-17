#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import randint
app = Flask(__name__)

randcollector = ""
@app.route(methods=['GET'])
def num_gen_6(max):
    for x in range (0, 8):
        rand = randint(0, 9)
        randcollector += str(rand)
	return jsonify({"Random Number":randcollector})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
