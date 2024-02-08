#!/usr/bin/env python3
"""Hashing password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns hashed password"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if a given password matches a previously hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
