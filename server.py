#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from flask import Flask, request, current_app
from flask_cors import CORS, cross_origin
from jsonp import jsonp
from flask import jsonify
app = Flask(__name__)
cors = CORS(app, resources={r"/api/users/*": {"origins": "*"}})

@app.route("/")
def hello():
    print os.environ.get('PYTHONSTARTUP')
    return "Hello World!"

@app.route("/api/jsonp/getCookie.js")
@jsonp
def getCookie():
    return jsonify({"foo":"bar","token":"1492499843375"})

@app.route("/api/users/me")
@cross_origin()
def me():
    return jsonify({
        "_id" : "57ee30ee5ffd454100714c6a",
        "email" : "liuwill@live.com",
        "modified" : "2017-04-17T03:28:40.866Z",
        "created" : "2017-04-17T03:28:40.866Z",
        "adsLeague" : 2,
        "useCytron" : True,
        "deny" : 0,
        "policyAgreed" : True,
        "status" : 2,
        "role" : "admin",
        "__v" : 0,
        "hashedPassword" : "",
        "salt" : "",
        "username" : "liuwei",
        "neverJoinAdsLeague" : True,
        "phone" : "15808652165",
        "masterRight" : 1,
        "secret" : ""
    })

if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
