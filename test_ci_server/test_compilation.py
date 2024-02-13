import unittest
import compileall

class CompilationTests(unittest.TestCase):
    '''
        Class containing compilation tests for `ci_server`.
    '''
    
    def test_compile_ci_logic(self):
        ''' 
            "Compiles" all files in the directory `ci_server`. Iff any file fails to compile 
            this test fails.
        '''

        res = compileall.compile_dir("ci_server", force=True, quiet=1)
        self.assertFalse(res, msg="Failed to compile the file sin ci_server")
