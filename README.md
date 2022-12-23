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
wrapper function[^1].

# Additional Notes

Some more miscallanea.

## Feature Requests

- Inspect the arguments provided and add value to the information given there.

## Devops Log

|&nbsp;|&nbsp;
|---|---
|**2022-12-23 08:30**|Docker artifacts were copied from the repository [`stephansamuel/poc-python-scripts`](https://github.com/stephansamuel/poc-python-scripts) and seemed to run generally well through base steps. Changed Python version, tag was `3.11-slim`, made it `3.7-slim`,  corresponding to `3.7.16 buster slim`, which more closely resembles target environment. Work stopped at `pip` upgrade. Removed `--root-user-action=ignore` from all `pip` directives, this doesn't seem to be supported on the lower version. Lower version also doesn't complain about running `pip` as `root` so this should be a good permanent fix to this. `docker-compose build` ran through otherwise. `up` runs, `nodemon` harness correctly facilitates CD process.
|**09:20**|Added VS Code extension [Markdown Footnotes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-footnotes) to allow inline implementation details in this doc. Also, CD environment doesn't always auto-reload after code changes. Will not fix at this time.

## Implementation

[^1]: given a passed arg of `callable`, the name (`str`) of the function can be
deduced automatically using the `__name__` property.