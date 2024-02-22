#!/usr/bin/env python3
"""auth Module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt."""
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_password