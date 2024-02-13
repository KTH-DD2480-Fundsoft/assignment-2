if __name__ == '__main__': exit()

import logging
from datetime import datetime



import os

class InfoOnlyFilter(logging.Filter):
    ''' 
        A filter for enforcing that the logger
        build_logger can only log at INFO level
    '''
    def filter(self, record):
        '''
            Filter method for enforcing that build_logger
            logs at INFO level. 

            Parameters
            ----------
            `record` : (`LogRecord`)
                The LogRecord that is being enforced.

            Returns
            -------
            `record.levelno == logging.INFO` : (`bool`)
                Boolean value enforcing the logging level.
        '''
        return record.levelno == logging.INFO


class Logger():
    ''' 
        A Logger class providing functions that log
        directly to `log/<date>.log` with timestamps
        and different logging levels. 
    '''

    def __init__(self, test=False):
        """
            Constructs a `Logger` which is simply a wrapper for two loggers from the
            module `logging`, named `Log` and `Build`, which will add their logging
            into their respective directories `log/` and `build_history/`.

            Parameters
            ----------
            `test` : (`bool`)
                bool determining if the Logger is run in a test enviornment or not.
                If true, store the logs in a separate .test.log file
        """
        test_str = ".test" if test else ""
        filename = datetime.now().strftime(f"%Y-%m-%d{test_str}.log")

        # The log message format
        log_str_format = '%(asctime)s - %(levelname)s: %(message)s'
        build_log_str_format = '%(asctime)s: %(message)s' # Remove INFO string from printout

        # Create a logger for standard log levels
        self.logger = logging.getLogger("Log")
        self.logger.setLevel(logging.DEBUG) # allows all log levels 
        if not os.path.exists("log"):
            os.makedirs("log", exist_ok=True)
        handler = logging.FileHandler(f"log/{filename}")
        formatter = logging.Formatter(log_str_format)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Create a logger for BUILD level logs
        self.build_logger = logging.getLogger("Build")
        self.build_logger.setLevel(logging.INFO)  # Only allow INFO level for BUILD
        if not os.path.exists("build_history"):
            os.makedirs("build_history", exist_ok=True)
        build_handler = logging.FileHandler(f"build_history/build_{filename}")
        build_formatter = logging.Formatter(build_log_str_format)
        build_handler.setFormatter(build_formatter)
        build_handler.addFilter(InfoOnlyFilter())  # Add the custom filter that only allows INFO level logs
        self.build_logger.addHandler(build_handler)

    def __del__(self):
        self._close()

    def _close(self):
        '''
            Close all handlers. Use with care, mainly for testing purposes.
        '''
        
        # for handler in self.logger.handlers + self.build_logger.handlers:
        #     handler.close()

        # test: trying to find why I get AttributeError: 'Logger' object has no attribute 'build_logger'
        handlers_to_close = self.logger.handlers
        if hasattr(self, 'build_logger'):
            handlers_to_close += self.build_logger.handlers
        for handler in handlers_to_close:
            handler.close()

    def debug(self, msg, *args): 
        '''
            Log message `msg` at the DEBUG level.

            Parameters
            ----------
            `msg` : (`str`)
                The message to log.
        '''

        self.logger.debug(msg, *args)

    def info(self, msg, *args):    
        '''
            Log message `msg` at the INFO level.

            Parameters
            ----------
            `msg` : (`str`)
                The message to log.
        '''

        self.logger.info(msg, *args)

    def warning(self, msg, *args): 
        '''
            Log message `msg` at the WARNING level.

            Parameters
            ----------
            `msg` : (`str`)
                The message to log.
        '''

        self.logger.warning(msg, *args)

    def error(self, msg, *args):   
        '''
            Log message at the ERROR level.

            Parameters
            ----------
            `msg` : (`str`)
                The message to log.
        '''

        self.logger.error(msg, *args)

    def log_build(self, build_info: dict):
        """
            Log a build status.
            
            <date time> - BUILD: BUILD <commit_id> SUCCESS/FAILURE: 
                <status_msg>

            Parameters
            ----------
            `build_info` : (`dict`)
                A dictonary containg:
                `success` : (`bool`)
                    Whether the build was a success or not.
                `commit_id` : (`str`)
                    The id of the commit tested.
                `status_msg` : (`str`)
                    Message containing, for example, an error message.
        """

        success = build_info["success"]
        commit_id = build_info["commit_id"]
        status_msg = build_info["status_msg"]

        log_str = f"BUILD {commit_id} "
        log_str += "SUCCESS" if success else "FAILURE"
        log_str += ": \n" + "\n".join(
            ['\t' + line for line in status_msg.splitlines()]
        )

        self.build_logger.info(log_str) # can only log at this level, any other level is filtered out
        self.logger.info(log_str) # can also log at DEBUG, ERROR and WARNING level
