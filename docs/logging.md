# Logging module documentation

## Class
The logging class, `Logger` is defined in `ci_server/logger.py` and is 
more or less a wrapper for the `Logger` class in the python library 
`logging`. This wrapper forces the logging to be to a specific file,
namely the file `log/<todays-date>.log`, and exposes four methods for
basic logging, `debug`, `info`, `warning` and `error`, these simply
add a log entry with corresponding logging level and a time stamp.

A special function `log_build` logs a build status at the log level 
`info`. This is the function to be used by the CI_logic module when
documenting CI results to be displayed in the web interface.

A special method `_close` is also defined as a way to close the opened
log file. To make testing possible.

### Example Usage

The module is used like so:
```python 
from logger import Logger 
log = Logger()
def my_func():
    log.debug("listening on 0.0.0.0:80")
    req = listen("0.0.0.0",80)
    if req.value == False:
        log.error("Got bad value from " + req.ip)
        do_something()
    else: 
        log.info("Got good value from " + req.ip)
        do_something_else()
```

