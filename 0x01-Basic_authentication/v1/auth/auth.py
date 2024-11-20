#!/usr/bin/env python3
"""Authentication module for the API.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage API authentication."""
    def authorization_header(self, request=None) -> str:
        """Returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None - request will be the Flask request object"""
        return None

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if path requires authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        
        if path[-1] != '/':
            path += '/'
            
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False
            elif excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False
                
        return True
