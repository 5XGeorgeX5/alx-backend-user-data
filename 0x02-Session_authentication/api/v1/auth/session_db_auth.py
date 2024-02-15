#!/usr/bin/env python3
"""class SessionDBAuth"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from os import getenv
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """class SessionDBAuth"""
    def __init__(self):
        """Initialize the class"""
        self.session_duration = int(getenv('SESSION_DURATION', '0'))

    def create_session(self, user_id=None):
        """Overload the create session method"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        user = UserSession(user_id=user_id, session_id=session_id)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Overload the user id for session id method"""
        try:
            user = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user:
            return None
        if self.session_duration <= 0:
            return user[0].user_id
        exp = user[0].created_at + timedelta(seconds=self.session_duration)
        if exp < datetime.utcnow():
            return None
        return user[0].user_id

    def destroy_session(self, request=None):
        """deletes the user session / logout"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            user = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not user:
            return False
        user[0].remove()
        return True
