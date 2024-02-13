#!/usr/bin/env python3
"""class to manage the API authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic authentication module"""
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts base64 authorization header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
