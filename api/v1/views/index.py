#!/user/bin/python3
"""
Index of app views
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status')
def status():
    """ route status"""
    status = {"status": "OK"}
    return jsonify(status)
