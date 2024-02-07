import subprocess
import unittest
import os 

CURRENT_PATH = os.path.abspath(__file__)
TMP_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

class CompilationTests(unittest.TestCase):
    def test_compile_file(self):
        # TODO: Uncomment and add the path when there are files to test
        path = TMP_PATH + "ci_server/logger2.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)