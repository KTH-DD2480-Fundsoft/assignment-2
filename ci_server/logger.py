if __name__ == '__main__': exit()

import logging
from datetime import datetime

class Logger():
    ''' 
        A Logger class providing functions that log
        directly to 'log/<date>.log' with timestamps
        and different logging levels. 
    '''

    def __init__(self, test=False):
        test_str = ".test" if test else ""
        filename = datetime.now().strftime(f"%Y-%m-%d{test_str}.log")

        # The log message format
        log_str_format = '%(asctime)s - %(levelname)s: %(message)s'
        
        # Create a logger and set it to write to todays logfile and 
        # to use a format with timestamp
        logger    = logging.Logger        ( "Log" )
        handler   = logging.FileHandler   ( f"log/{filename}" )
        formatter = logging.Formatter     ( log_str_format )
        handler.setFormatter ( formatter )
        logger.addHandler    ( handler )
        self.logger = logger
    def __del__(self): self._close()
    def _close(self):
        ''' Close all handlers. Use with care, mainly for testing purposes. '''
        [handler.close() for handler in self.logger.handlers]
    def debug(self, msg, *args): 
        ''' Log message at level DEBUG '''   
        self.logger.debug (msg, *args)
    def info(self, msg, *args):    
        ''' Log message at level INFO'''   
        self.logger.info  (msg, *args)
    def warning(self, msg, *args): 
        ''' Log message at level WARNING'''   
        self.logger.warning  (msg, *args)
    def error(self, msg, *args):   
        ''' Log message at level ERROR'''   
        self.logger.error (msg, *args)
    def log_build(self, build_info : dict):
        ''' 
            Log a build status.
            
            <date time> - INFO: BUILD <commit_id> SUCCESS/FAILURE: 
                <status_msg>

            :param build_info: A dictionary containng 
                'success : bool' -- whether build was a success or not
                'commit_id : str' -- the id of the commit tested
                'status_msg : str' -- message containing, for example, error message.

        '''  
        success = build_info["success"]
        commit_id = build_info["commit_id"]
        status_msg = build_info["status_msg"]

        log_str = f"BUILD {commit_id} "
        log_str += "SUCCESS" if success else "FAILURE"
        log_str += ": \n" + "\n".join(
                    ['\t' + line for line in status_msg.splitlines()]
                )
       
        self.info(log_str)




