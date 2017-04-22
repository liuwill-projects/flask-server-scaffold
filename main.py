#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from flask import Flask, jsonify # , request, current_app
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, emit, send
from chat.utils.jsonp import jsonp
from chat.controllers.mock import Mock
import logging
from logging.config import fileConfig

fileConfig('logging_config.ini')
logger = logging.getLogger()
#logger = logging.getLogger('api')

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

@socketio.on('message', namespace='/chat')
def handle_message(message):
    send(message)

@socketio.on('json', namespace='/chat')
def handle_json(json):
    send(json, json=True)

@socketio.on('my event', namespace='/chat')
def test_message(message):
    emit('my response', {'data': 'got it!'})

@socketio.on('connect', namespace='/chat')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/chat')
def test_disconnect():
    print('Client disconnected')

if __name__ == "__main__":
    #app.run('0.0.0.0', 5000)
    socketio.run(app, host='0.0.0.0', port=5000)
