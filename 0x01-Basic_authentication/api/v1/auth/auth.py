#!/usr/bin/env python3
""" authentication module
"""
from typing import List, TypeVar
from flask import request


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
        return (path not in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None
