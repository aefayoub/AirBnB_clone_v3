#!/usr/bin/python3
"""API Entry Point."""
from builtins import KeyError
from flask import Flask, jsonify
from models import storage
import os
from v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Teardown handling.

    Closes the database connection when the application context is torn down.
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """Handle page 404.

    Returns a JSON response with a 404 error message.
    """
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
