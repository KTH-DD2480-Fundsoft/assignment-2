import unittest
import compileall

class CompilationTests(unittest.TestCase):

    def test_compile_ci_logic(self):
        try:     
            compileall.compile_dir("ci_server", force=True)
            pass
        except Exception as e:
            self.fail(f"Compilation error: {str(e)}")
