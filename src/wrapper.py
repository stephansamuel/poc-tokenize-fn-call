from functools import wraps

def poc_instrumentation_wrapper(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        called_name: str = f.__name__
        print(f"+ FN: {called_name}")
        result = f(*args, **kwargs)
        print(f"- result: {result}")
        return result
    return wrapper