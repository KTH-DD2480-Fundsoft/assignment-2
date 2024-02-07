import os
import subprocess
from tests import run_tests
"""
Contains logic for the the continuous integration server
"""

CURRENT_PATH = os.path.abspath(__file__)
TMP_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

def continuous_integration(commit_hash):
    pull_repo(commit_hash)

    print("Running tests")
    test_result = run_tests()
    if test_result.wasSuccessful():
        print("Tests passed")
    else:
        print("Tests failed")
        print(test_result.failures)
        print(test_result.errors)

    update_commit_status(commit_hash, test_result.wasSuccessful())

    remove_repo()

def pull_repo(commit_hash):
    """
    Pulls the repository from the remote server
    """
    repo_url = "git@github.com:KTH-DD2480-Fundsoft/assignment-2.git"

    subprocess.run(["git", "clone", repo_url, TMP_PATH])
    os.chdir(TMP_PATH)
    subprocess.run(["git", "checkout", commit_hash])

def remove_repo():
    """
    Removes the repository from the local server
    """
    subprocess.run(["rm", "-rf", TMP_PATH])

def valid_directory():
    """ 
    Checks that TMP_RELATIVE_PATH exists and contains the directories
    """
    """
    ci_server = TMP_PATH + "ci-server"
    doc = TMP_PATH + "doc"

    return os.path.isdir(TMP_PATH) and os.path.isdir(ci_server) and os.path.isdir(doc)    
    """
    pass

def update_commit_status(commit_hash, status):
    """
    Updates the commit status on the remote server
    """
    pass
    

if __name__ == "__main__":
    continuous_integration("9db4097800643a82f017ef626bf1cd5322750101")
