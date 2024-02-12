import unittest
from ci_server.ci_logic import continuous_integration

class CIUnitTests(unittest.TestCase):
    def test_print_hello_world(self):
        self.assertTrue(continuous_integration("6a13a8dc2a28d0000be5aff4ec93065608555cc3"))
        pass
