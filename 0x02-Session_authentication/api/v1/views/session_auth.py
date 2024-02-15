#!/usr/bin/env python3
"""handles all routes for the Session authentication"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route(
        '/auth_session/login',
        methods=['POST'],
        strict_slashes=False
        )
def session_login():
    """POST /api/v1/auth_session/login"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    response = jsonify(user[0].to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)
    return response


@app_views.route(
        'auth_session/logout',
        methods=['DELETE'],
        strict_slashes=False
        )
def session_logout():
    """DELETE /api/v1/auth_session/logout"""
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({})
    abort(404)
