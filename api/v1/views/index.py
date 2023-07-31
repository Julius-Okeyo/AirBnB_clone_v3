#!/usr/bin/python3
"""
json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    returns status of a GET request
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)

