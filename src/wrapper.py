#from datetime import time
from functools import wraps
from typing import List, Dict, NamedTuple
import uuid

class ParsedFn(NamedTuple):
    called: str
    tokenized: object = None
    #parse_args: callable = None

class FunctionParser:
    
    def parse_fn(self, name: str) -> ParsedFn:
        # This is a degenerate implementation; subclass.
        return ParsedFn(name)

class FnCall(NamedTuple):
    #context: str
    call: str
    #args: List[object]
    #kwargs: Dict[str, object]
    parsed: List[ParsedFn]
    #started: time
    #ended: time
    #result: object
    unique_id: uuid.UUID = uuid.uuid4()

class PocInstrumentation:

    _fn_parsers: List[FunctionParser] = []

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
            result = f(*args, **kwargs)
            call = FnCall(
                called_name,
                #args,
                #kwargs,
                PocInstrumentation._execute_parsers(called_name)
                #result
            )
            print(f"+ FN: {call}")
            return result
        return wrapper

