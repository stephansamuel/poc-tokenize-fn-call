import arcpy
from wrapper import FunctionParser, ParsedFn

class TrivialParser(FunctionParser):

    def parse_fn(self, name: str) -> ParsedFn:
        #print(dir(arcpy))
        def flt(fn: str) -> bool:
            return not (fn.startswith("__") or fn.endswith("__"))
        mock = [fn for fn in dir(arcpy) if flt(fn)]
        if name in mock:
            print(f"* found {name}")

        # This is a degenerate implementation; subclass.
        return ParsedFn(name)
