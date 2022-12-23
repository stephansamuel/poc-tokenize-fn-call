import wrapper

inst = wrapper.PocInstrumentation()
inst.add_parser(wrapper.FunctionParser())

@inst.fn_inst
def i_am_a_function(a: str, b: str = None) -> str:
    result: str = f"Hello, world! {a} {b}"
    print(result)
    return result

if __name__ == "__main__":
    i_am_a_function("a_val", b="b_val")
