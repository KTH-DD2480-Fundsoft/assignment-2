import subprocess
import unittest

class CompilationTests(unittest.TestCase):
    def test_compile_file(self):
        path = "ci_server/logger.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)