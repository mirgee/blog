from flask import redirect, Response
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))


class ModelView(ModelView):
    def is_accessible(self, basic_auth):
        if not basic_auth.authenticate():
            raise AuthException('Not authenticated.')
        return True

    def inaccessible_callback(self, name, basic_auth, **kwargs):
        return redirect(basic_auth.challenge())
