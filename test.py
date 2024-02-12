import unittest
'''
Runs all unittest and prints the errors/failures in a parseable way.
'''
if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover("test_ci_server")
    runner = unittest.TextTestRunner()
    res =  runner.run(tests)
    errors = [f"Error in {type(tc).__name__}:{err}\n" for tc,err in res.errors]
    failures = [f"Error in {type(tc).__name__}:{err}\n" for tc,err in res.errors]
    print((errors,failures))



