from datetime import datetime, timedelta
import unittest
import ci_server.logger

import os


class TestLogger(unittest.TestCase):
    '''
        Class containing tests for `ci_server/logger.py`.
    '''

    @classmethod
    def setUpClass(cls):
        cls.logger = ci_server.logger.Logger(test=True)


    def setUp(self):
        self.max_time_since_created_last_build_log = 10 # milliseconds

        self.build_dir = 'build_history'

        build_files = os.listdir(self.build_dir)
        if not build_files:
            self.fail(f'no directory "{self.build_dir}" found')
        build_files.sort(reverse=True)  # Sort files in reverse alphabetical order
        self.latest_build_file = build_files[0] # The name of the file last in alphabetical order in 'build_history', the one most recently created

        self.build_file_path = os.path.join(self.build_dir, self.latest_build_file) # latest build file path
        self.log_file_path = datetime.now().strftime("log/%Y-%m-%d.test.log")


    
    def test_latest_build_log_file_path(self):
        ''' 
            Test that the file last in alphabetical order in the dir `build_history`
            was created no more than 10 milliseconds ago
        '''

        # Extract timestamp from filename
        filename_parts = self.latest_build_file[6:32] # extract only the time stamp part of the file name
        file_timestamp = datetime.strptime(filename_parts, "%Y-%m-%d_%H-%M-%S-%f")

        # Calculate current time and compare
        current_time = datetime.now()
        time_difference = current_time - file_timestamp

        # Assert that the time difference is at least max_time_since_created_last_build_log milliseconds
        self.assertLessEqual(time_difference, timedelta(milliseconds=self.max_time_since_created_last_build_log),
                                f"Latest file '{self.latest_build_file}' does not represent a time no more than {self.max_time_since_created_last_build_log} milliseconds ago.")
    

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

        self.logger.debug("test1")
        self.logger.info("test2")
        self.logger.warning("test3")
        self.logger.error("test4")
        f = open(self.log_file_path)
        lines = f.readlines()
        l1 = lines[-4]
        l2 = lines[-3]
        l3 = lines[-2]
        l4 = lines[-1]
        self.assertTrue("DEBUG: test1"   in l1, msg = f'"DEBUG: test1" not found in {l1}')
        self.assertTrue("INFO: test2"    in l2, msg = f'"INFO: test2" not found in {l2}')
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
            date = datetime.strptime(l.split(' - ')[0],"%Y-%m-%d %H:%M:%S,%f")
            if date - datetime.now() > timedelta(milliseconds=10):
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
    
    def tearDown(self):
        ''' 
            Clears the content of the test log file
        '''
        open(self.log_file_path, 'w').close()