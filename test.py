#!/usr/bin/python3
''' 
Runs all unit and system tests in the directory 'test_ci-server' with file prefix "test_". 
This also includes files in subdirectories
'''
import unittest

loader = unittest.TestLoader()
tests = loader.discover('test_ci-server')

test_runner = unittest.TextTestRunner()
test_runner.run(tests)