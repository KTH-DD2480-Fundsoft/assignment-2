#!/usr/bin/python3
''' 
Runs all unit and system tests in the directory 'test_ci_server' in tmp with file prefix "test_". 
This also includes files in subdirectories
'''
import unittest
import os

CURRENT_PATH = os.path.abspath(__file__)
TEST_CI_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/test_ci_server")
TMP_CI_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

def run_tests():
    os.chdir(TMP_CI_PATH)
    loader = unittest.TestLoader()
    tests = loader.discover(TEST_CI_PATH)

    test_runner = unittest.TextTestRunner()
    result = test_runner.run(tests)
    return result
