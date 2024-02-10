import os
import subprocess
from ci_server.test_runner import run_tests
from ci_server.logger import Logger

"""
Contains logic for the the continuous integration server
"""

CURRENT_PATH = os.path.abspath(__file__)
TMP_PATH = os.path.join(os.path.dirname(CURRENT_PATH), "../tmp/")

def continuous_integration(commit_hash):
    logger = Logger()
    
    logger.info(f"Pulling repository with hash {commit_hash}")
    pull_repo(commit_hash)

    logger.info("Running tests")
    output, error = run_tests()
    
    # TODO: Add better way of determining a successful run
    successful_run = ("OK" in output or "OK" in error)

    build_dict = {"commit_id" : commit_hash}
    if successful_run:
        build_dict["success"] = True
        build_dict["status_msg"] = "Success"
    else:
        build_dict["success"] = False
        build_dict["status_msg"] = error

    logger.log_build(build_dict)

    logger.info("Updating commit status")
    update_commit_status(commit_hash, successful_run)

    logger.info("Removing repository")
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

def update_commit_status(commit_hash, status):
    """
    Updates the commit status on the remote server
    """
    pass
    

if __name__ == "__main__":
    # Only used for debugging purposes
    continuous_integration("8bb44dc4dc9bdca324c40ae5e2d824009c083a69")
