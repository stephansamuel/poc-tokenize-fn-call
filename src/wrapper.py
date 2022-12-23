from functools import wraps
from typing import List, NamedTuple

class ParsedFn(NamedTuple):
    called: str
    tokenized: object = None
    parse_args: callable = None

class FunctionParser:
    
    def parse_fn(self, name: str) -> ParsedFn:
        # This is a degenerate implementation; subclass.
        return ParsedFn(name)

class PocInstrumentation:

    _fn_parsers: List[FunctionParser]

    def __init__(self):
        if not self._fn_parsers:
            self._fn_parsers = []
    
    @classmethod
    def add_parser(cls, parser: FunctionParser) -> None:
        cls._fn_parsers.append(parser)

    @classmethod
    def _execute_parsers(cls, fn: str) -> List[ParsedFn]:
        if not cls._fn_parsers:
            return
        return [parser.parse_fn(fn) for parser in cls._fn_parsers]

    # This should have a decorator like @staticmethod but convention doesn't
    # seem to warrant that and it seems to work perfectly fine as a static
    # method without.
    def fn_inst(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            called_name: str = f.__name__
            print(f"+ FN: {called_name}")
            result = f(*args, **kwargs)
            print(f"- result: {result}")
            return result
        return wrapper

