#!/usr/bin/python3
"""API Entry Point."""
from api.v1.views import app_views
from builtins import KeyError
import os
from flask import Flask, jsonify
from models import storage
app = Flask(__name__)
app.register_blueprint(app_views)


# Define a teardown function to close the database connection
@app.teardown_appcontext
def teardown(self):
    """Teardown handling."""
    storage.close()


# Define an error handler for 404 Not Found errors
@app.errorhandler(404)
def page_not_found(error):
    """Handle page 404."""
    status = {"error": "Not found"}
    return jsonify(status), 404


# Entry point to run the application
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
