import os
import subprocess
from ci_server.GitHub_API_functions import create_commit_status
from ci_server.test_runner import run_tests
from ci_server.logger import Logger

"""
Contains logic for the the continuous integration server
"""

PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_PATH = os.path.join(PROJ_ROOT, "tmp/")

def continuous_integration(commit_hash):
    logger = Logger()
    
    logger.info(f"Pulling repository with hash {commit_hash}")
    pull_repo(commit_hash)

    logger.info("Running tests")
    errors, failures = run_tests()
    
    # TODO: Add better way of determining a successful run
    successful_run = not errors and not failures  

    build_dict = {"commit_id" : commit_hash}
    if successful_run:
        build_dict["success"] = True
        build_dict["status_msg"] = "Success"
        commit_status = 'success'
    else:
        build_dict["success"] = False
        build_dict["status_msg"] = errors + failures 
        commit_status = 'error' if errors else 'failure'

    logger.log_build(build_dict)

    logger.info("Updating commit status")
    
    create_commit_status(commit_hash, commit_status)

    logger.info("Removing repository")
    remove_repo()

    return successful_run

def pull_repo(commit_hash):
    """
    Pulls the repository from the remote server
    """
    repo_url = "git@github.com:KTH-DD2480-Fundsoft/assignment-2.git"

    subprocess.run(["git", "clone", repo_url, TMP_PATH])
    os.chdir(TMP_PATH)
    try: 
        subprocess.run(["git", "checkout", commit_hash])
    finally: 
        os.chdir(PROJ_ROOT)

def remove_repo():
    """
    Removes the repository from the local server
    """
    subprocess.run(["rm", "-rf", TMP_PATH])
    subprocess.run(["mkdir", TMP_PATH])


if __name__ == "__main__":
    # Only used for debugging purposes
    continuous_integration("8bb44dc4dc9bdca324c40ae5e2d824009c083a69")
