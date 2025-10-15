from flask import Flask, redirect, jsonify
from .service import URLShortnerService

app = Flask(__name__)

@app.get('/<shorturl>')
def redirect_to_long_url(shorturl):
    return redirect()

@app.post('/shorten')
def create_short_url():
    return jsonify({
        'short_url': 
    }), 201


    