#!/usr/bin/python3
"""Index of app views."""
from flask import jsonify
from models import storage
from api.v1.views import app_views


# Function: status
@app_views.route('/status')
def status():
    """Route status."""
    status = {"status": "OK"}
    return jsonify(status)


# Function: status
@app_views.route('/stats')
def count():
    """Return count of object."""
    total = {}
    classes = {"Amenity": "amenities",
               "City": "cities",
               "Place": "places",
               "Review": "reviews",
               "State": "states",
               "User": "users"}
    for cls in classes:
        count = storage.count(cls)
        total[classes.get(cls)] = count
    return jsonify(total)
