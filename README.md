# Function Call Tokenization <small>Python | Proof of Concept</small>

This functional code block demonstrates a fixture that [`@wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)
a function call and deduces more information about it.

The call is at runtime so it is not expected to replace static code analysis.
Rather, it allows more sophisticated runtime instrumentation where it is used,
and SCA may be a valid way in which to insert it into existing code
programatically.

## Design

Little attantion has been paid to the design of the wrapper. Assume a general
reference implementation. Of note, deduce the function call (as `str`) from the
wrapper function.

# Additional Notes

Some more miscallanea.

## Feature Requests

- Inspect the arguments provided and add value to the information given there.
