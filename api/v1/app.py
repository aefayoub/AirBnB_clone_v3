#!/usr/bin/python3
"""The API entry point to run the app."""
from builtins import KeyError
from flask import Flask, jsonify
from models import storage
import os
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


# Closes the database connection when the application
@app.teardown_appcontext
def teardown(self):
    """Found database connection when the application."""
    storage.close()


# Returns a JSON response with a 404 error message
@app.errorhandler(404)
def page_not_found(error):
    """Return a JSON response with a 404."""
    status = {"error": "Not found"}
    return jsonify(status), 404


if __name__ == '__main__':
    # Retrieve the host and port from environment variables.
    try:
        host = os.environ.get('HBNB_API_HOST')
    except KeyError:
        host = '0.0.0.0'

    try:
        port = os.environ.get('HBNB_API_PORT')
    except KeyError:
        port = '5000'

    # Run the Flask application with the specified host and port
    app.run(host=host, port=port)
