# #######################################################
# # added this block to solve ModuleNotFoundError
# #######################################################
# import sys
# import os
# # Get the absolute path of the parent directory
# project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # Add the parent directory to sys.path
# sys.path.append(project_dir)
# # Print out sys.path to verify that the directory has been added
# # print(sys.path)
# #######################################################




import datetime
import unittest
import ci_server.logger


class TestLogger(unittest.TestCase):
    '''
        Class containing tests for `ci_server/logger.py`.
    '''
    
    log_file_path = datetime.datetime.now().strftime("log/%Y-%m-%d.test.log")
    build_file_path = datetime.datetime.now().strftime("log/%Y-%m-%d.test.log")
    logger = ci_server.logger.Logger(test=True)

    def test_file_path(self):
        ''' 
            Test if the logfile has been created and named after today's date.
        '''

        try: 
            f = open(self.log_file_path)
            f.close()
        except FileNotFoundError as e: self.fail(str(e) + "Can't open logfile")

    def test_writes(self):
        ''' 
            Test if the logger writes the given string as is, with the format 
            given in `logger.py`
        '''

        f = open(self.log_file_path)
        f.seek(0,2)
        self.logger.debug("test1")
        self.logger.info("test2")
        self.logger.warning("test3")
        self.logger.error("test4")
        l1 = f.readline()
        l2 = f.readline()
        l3 = f.readline()
        l4 = f.readline()
        self.assertTrue("DEBUG: test1"   in l1, msg = "Wrong format when writing DEBUG log")
        self.assertTrue("INFO: test2"    in l2, msg = "Wrong format when writing INFO log")
        self.assertTrue("WARNING: test3" in l3, msg = "Wrong format when writing WARNING log")
        self.assertTrue("ERROR: test4"   in l4, msg = "Wrong format when writing ERROR log")
        f.close() 

    def test_date(self):
        ''' 
            Tests if the logger prints the timestamp in the correct format.
        '''

        f = open(self.log_file_path)
        f.seek(0,2)
        self.logger.info("42")
        l = f.readline()
        try: 
            date = datetime.datetime.strptime(l.split(' - ')[0],"%Y-%m-%d %H:%M:%S,%f")
            if date - datetime.datetime.now() > datetime.timedelta(microseconds=10):
                raise ValueError()
        except: self.fail("Time format in log is wrong!")
        finally: f.close()


    def test_build_logger(self):
        '''
            Tests that logger.log_build writes to the file in the correct format.
        '''

        f = open(self.build_file_path)
        f.seek(0,2)
        build_data = {"success" : True, "commit_id" : "123456", "status_msg" : "some message"}
        self.logger.log_build(build_data)
        data = f.read() 
        f.close()
        self.assertTrue("SUCCESS" in data and "123456" in data and "some message" in data)
