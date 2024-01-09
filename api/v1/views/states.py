#!/usr/bin/python3
"""
State view that contains all methods
"""

from flask import abort, jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def states_all():
    """return all states"""
    states = []
    states = storage.all("State").values()
    for state in states:
        states.append(state.to_json())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'])
def states_get(state_id):
    """return all state by id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state = state.to_json()
    return jsonify(state)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def states_delete(state_id):
    """delete state by id"""
    empty_dict = {}
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify(empty_dict), 200
