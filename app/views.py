from app import app
import json
import requests

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"