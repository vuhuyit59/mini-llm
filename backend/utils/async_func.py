import asyncio
import nest_asyncio


def run_async_from_sync(func, *args, **kwargs):
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # 'RuntimeError: There is no current event loop...'
        loop = None
    if loop and loop.is_running():
        nest_asyncio.apply()
        result = loop.run_until_complete(func(*args, **kwargs))
        return result
    else:
        result = asyncio.run(func(*args, **kwargs))
    return result
