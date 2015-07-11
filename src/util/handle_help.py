from functools import wraps
from flask import request, jsonify
from flask.ext.restful import reqparse

help_messages = {
    'station': """
        Allowed query parameters are:
            period: today
    """
}

def handle_help(key):

    def wrapper(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if request.args.get('help'):
                return help_messages.get(key, "No help for this route")
            return func(*args, **kwargs)
        return decorated_function
    return wrapper
