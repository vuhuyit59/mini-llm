from asyncio import run
from functools import wraps


def async_command(app, *args, **kwargs):
    def decorator(async_func):
        @wraps(async_func)
        def sync_func(*_args, **_kwargs):
            return run(async_func(*_args, **_kwargs))

        app.command(*args, **kwargs)(sync_func)

        return async_func

    return decorator
