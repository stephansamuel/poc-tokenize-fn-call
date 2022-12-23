import wrapper

inst = wrapper.PocInstrumentation()
inst.add_parser(wrapper.FunctionParser())

@inst.fn_inst
def i_am_a_function():
    print("Hello, world!")
    pass

if __name__ == "__main__":

    i_am_a_function()
