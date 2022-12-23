from functools import wraps

class PocInstrumentation:

    def fn_inst(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            called_name: str = f.__name__
            print(f"+ FN: {called_name}")
            result = f(*args, **kwargs)
            print(f"- result: {result}")
            return result
        return wrapper

