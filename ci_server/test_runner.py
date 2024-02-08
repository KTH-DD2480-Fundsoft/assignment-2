#!/usr/bin/python3
''' 
Runs all unit and system tests in the directory 'test_ci_server' in tmp with file prefix "test_". 
This also includes files in subdirectories
'''
import os
import subprocess

CURRENT_PATH = os.path.abspath(__file__)
TEST_CI_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/test_ci_server")
TMP_CI_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

def run_tests():
    os.chdir(TMP_CI_PATH)
    cmd = ['python3', '-m', "unittest", "discover", "test_ci_server/"]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode("utf-8"), result.stderr.decode("utf-8")
