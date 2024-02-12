import unittest
if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.discover("test_ci_server")
    runner = unittest.TextTestRunner()
    res =  runner.run(tests)
    errors = [f"Error in test case '{tc}'\n" for tc,_ in res.errors]
    failures = [f"Failure in test case '{tc}'\n" for tc,_ in res.failures]
    print((errors,failures))



