#!/usr/bin/env python3
"""class to manage the API authentication"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User
import uuid


class SessionAuth(Auth):
    """Session authentication module"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session for a user"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns the user id by their session id"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Current user"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        if session_id not in self.user_id_by_session_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
