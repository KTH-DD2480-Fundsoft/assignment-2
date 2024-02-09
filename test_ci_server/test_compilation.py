import subprocess
import unittest

class CompilationTests(unittest.TestCase):

    def test_compile_ci_logic(self):
        path = "ci_server/ci_logic.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)

    def test_compile_logger(self):
        path = "ci_server/logger.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)

    def test_compile_server(self):
        path = "ci_server/server.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)
    
    def test_compile_test_runner(self):
        path = "ci_server/test_runner.py"
        result = subprocess.run(['python', '-m', 'py_compile', path], capture_output=True, text=True)
        self.assertTrue(result.returncode == 0, result.stderr)