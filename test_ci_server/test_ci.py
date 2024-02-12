import unittest
from ci_server.ci_runner import continuous_integration

class CIUnitTests(unittest.TestCase):
    def test_bad_commit(self):
        ''' Runs the CI tests on a commit with always passing tests '''
        self.assertFalse(continuous_integration("521cbec8cb335afa7e490e324b7e92fd75e9e6e8"))
        pass
    def test_good_commit(self):
        ''' Runs the CI tests on a commit with always passing tests '''
        self.assertTrue(continuous_integration("4e0b618f7caf520675157c5b35a7ebaab7c23320"))
        pass
