#!/usr/bin/env python3
"""class to manage the API authentication"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes base64 authorization header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            decode_base = base64.b64decode(
                base64_authorization_header.encode())
            value = decode_base.decode('utf-8')
            return value
        except Exception:
            return None
