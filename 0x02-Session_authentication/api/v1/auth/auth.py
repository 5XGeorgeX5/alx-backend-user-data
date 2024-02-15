#!/usr/bin/env python3
""" authentication module
"""
from typing import List, TypeVar
from flask import request
from os import getenv


TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S"
DATA = {}


class Auth():
    """Authentication class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks the required path"""
        if path is None or excluded_paths is None:
            return True
        if path[-1] != "/":
            path += "/"
        for excluded in excluded_paths:
            if excluded[-1] == "/":
                if path == excluded:
                    return False
            elif path.startswith(excluded[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """validates all requests to secure the API"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
