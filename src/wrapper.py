from functools import wraps
import time
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
    args: List[object]
    kwargs: Dict[str, object]
    parsed: List[ParsedFn]
    started: float
    ended: float
    result: object
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

    def fn_inst(_, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            called_name: str = f.__name__
            started = time.perf_counter()
            result = f(*args, **kwargs)
            ended = time.perf_counter()
            call = FnCall(
                called_name,
                args,
                kwargs,
                PocInstrumentation._execute_parsers(called_name),
                started,
                ended,
                result
            )
            print(f"+ FN: {call}")
            return result
        return wrapper

