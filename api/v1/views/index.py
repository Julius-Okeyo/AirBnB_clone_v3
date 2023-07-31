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

@app_views.route('/stats', methods=['GET'])
def stats():
    """
    return count of objects by type(class)
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)
