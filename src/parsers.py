import arcpy
from functools import reduce
import inspect
import sys
from typing import List, Tuple
from wrapper import FunctionParser, ParsedFn

class TrivialParser(FunctionParser):

    def parse_fn(self, name: str) -> ParsedFn:

        '''
        def flt(fn: str) -> bool:
            return not (fn.startswith("__") or fn.endswith("__"))
        mock = [fn for fn in dir(arcpy) if flt(fn)]
        if name in mock:
            print(f"* found {name}")
        '''

        '''
        fn = get_fn_from_name(name)
        code = get_calls_from_fn(fn)
        print(code)
        '''

        print(dict(sys.modules.copy()))

        # This is a degenerate implementation; subclass.
        return ParsedFn(name)

def get_fn_from_name(name: str) -> callable:
    all_globals = globals().copy()
    all_globals.update(locals())
    fn = all_globals.get(name)
    if not fn:
        raise RuntimeError(f"could not find method {name}")
    return fn

def get_calls_from_fn(fn: callable) -> List[str]:
    code_lines = inspect.getsource(fn)
    return code_lines

def get_names_of_all_loaded_modules() -> List[str]:
    def flt(mod: str) -> bool:
        return not mod.startswith("_")
    all_modules = list(sys.modules.copy().keys())
    all_modules.sort()
    return [m for m in all_modules if flt(m)]

def get_all_defined_functions() -> List[Tuple[str, object]]:
    def red(mod: str):
        pass