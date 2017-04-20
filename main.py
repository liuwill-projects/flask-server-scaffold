#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from flask import Flask, jsonify # , request, current_app
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit
from chat.utils.jsonp import jsonp
from chat.controllers.mock import Mock

app = Flask(__name__)
cors = CORS(app, resources={r"/api/users/*": {"origins": "*"}})
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
mockController = Mock(app)

@app.route("/")
def hello():
    print os.environ.get('PYTHONSTARTUP')
    return "Hello World!"

@app.route("/api/jsonp/getCookie.js")
@jsonp
def getCookie():
    return mockController.getCookie()

@app.route("/api/users/me")
@cross_origin()
def me():
    return mockController.me()

@socketio.on('my event')
def test_message(message):
    emit('my response', {'data': 'got it!'})

if __name__ == "__main__":
    #app.run('0.0.0.0', 5000)
    socketio.run(app, host='0.0.0.0', port=5000)
