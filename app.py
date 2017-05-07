import os
from flask import Flask
import json

'''
from flask import Flask, request
import json
import requests
'''

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<user>')
def profile(user):
    return '<h2>Tuna is good %s</h2>' % user

@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h2>Tuna is good %s</h2>' % post_id

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
