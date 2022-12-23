from wrapper import FunctionParser, ParsedFn

class TrivialParser(FunctionParser):

    def parse_fn(self, name: str) -> ParsedFn:
        #import arcpy
        #print(dir(arcpy))

        # This is a degenerate implementation; subclass.
        return ParsedFn(name)
