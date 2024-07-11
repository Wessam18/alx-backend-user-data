#!/usr/bin/env python3
"""
    Auth class
"""
from typing import List, TypeVar
import os


class Auth:
    """Define Auth Class"""
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """Return False for excluded paths, True otherwise"""
        if path is None:
            return True
        if not excluded_paths or len(excluded_paths) == 0:
            return True
        for excluded_path in excluded_paths:
            wildcard = excluded_path[:-1]
            if excluded_path.endswith('*') and path.startswith(wildcard):
                return False
            elif path == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Return None
        """
        return None

    def session_cookie(self, request=None):
        """
            returns a cookie value from a request
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name)
