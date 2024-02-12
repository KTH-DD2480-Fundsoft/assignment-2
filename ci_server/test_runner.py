#!/usr/bin/python3
''' 
Runs all unit and system tests in the directory 'test_ci_server' in tmp with file prefix "test_". 
This also includes files in subdirectories
'''
import os
import subprocess
import ast 

PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_PATH = os.path.join(PROJ_ROOT, "tmp/")

def run_tests():
    os.chdir(TMP_PATH)
    errors = ["INTERNAL FAILURE"]
    failures = []
    try:
        cmd = ['python3', "test.py"]
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        errors, failures = ast.literal_eval(result.stdout.decode("utf-8"))
    finally:
        os.chdir(PROJ_ROOT)
        return errors, failures 
