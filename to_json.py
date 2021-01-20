import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrapped
