#!/user/bin/python3
"""
Index of app views
"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """ route status"""
    status = {"status": "OK"}
    return jsonify(status)

@app_views.route('/stats')
def count():
    """ returns count of objects"""
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
