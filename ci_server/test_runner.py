#!/usr/bin/python3
''' 
Runs all unit and system tests in the directory 'test_ci_server' in tmp with file prefix "test_". 
This also includes files in subdirectories
'''
import os
import subprocess
import ast 

CURRENT_PATH = os.path.abspath(__file__)
TMP_CI_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

def run_tests():
    os.chdir(TMP_CI_PATH)
    cmd = ['python3', "test.py"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    errors, failures = ast.literal_eval(result.stdout.decode("utf-8"))
    return errors, failures 
