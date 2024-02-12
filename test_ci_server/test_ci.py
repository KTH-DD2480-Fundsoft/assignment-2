import unittest

class CIUnitTests(unittest.TestCase):
    def test_return_true(self):
        return True
    def test_fail(self):
        self.fail("This is supposed to fail")
    def test_error(self):
        raise Exception("This is an error")
