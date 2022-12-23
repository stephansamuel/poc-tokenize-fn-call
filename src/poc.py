import wrapper

@wrapper.poc_instrumentation_wrapper
def i_am_a_function():
    print("Hello, world!")
    pass

if __name__ == "__main__":
    i_am_a_function()
