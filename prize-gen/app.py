#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import randint
app = Flask(__name__)

@app.route(methods=['GET'])
def prizegen():
	rand = randint(0,100)
	if rand <= 25:
		return jsonify({"Random Prize":2000})
	elif rand > 25:
		return jsonify({"Random Prie":1000})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)
