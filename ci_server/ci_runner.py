from ci_server import log
import os
import subprocess
from ci_server.GitHub_API_functions import create_commit_status
from ast import literal_eval
"""
Contains logic for the the continuous integration server
"""


PROJ_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP_PATH = os.path.abspath(os.path.join(PROJ_ROOT, "tmp/"))

def continuous_integration(commit_hash):
    '''
        Runs the continous integration process for the commit identified by
        `commit_hash`, where the repository is cloned, tests are executed,
        the results are logged and the commit status is updated. The results
        are logged in the directory `build_history/`.

        Parameters
        ----------
        `commit_hash` : (`str`)
            The sha256 hash of the commit to be build tested.

        Returns
        ----------
        `successful_run` : (`bool`)
            `True` if the CI was successful, otherwise `False`.
    '''
    try:
        
        log.info(f"Pulling repository with hash {commit_hash}")
        pull_repo(commit_hash)
    
        log.info("Running tests")
        errors, failures = run_tests()
        print(errors,failures) 
        # TODO: Add better way of determining a successful run
        successful_run = not errors and not failures  

        build_dict = {"commit_id" : commit_hash}
        if successful_run:
            build_dict["success"] = True
            build_dict["status_msg"] = "Success"
            commit_status = 'success'
        else:
            build_dict["success"] = False
            build_dict["status_msg"] = '\n'.join(errors + failures)
            commit_status = 'error' if errors else 'failure'

        log.log_build(build_dict)

        log.info("Updating commit status")
        
        create_commit_status(commit_hash, commit_status)

        log.info("Removing repository")
        remove_repo()

        return successful_run
    except Exception as e:
        log.error(f"Fatal error: {str(e)}\n\t sending error to GH.")
        try: create_commit_status(commit_hash,"error")
        except Exception as ce: log.error(commit_hash, "failed to send error!")
        finally: return False
def run_tests():
    ''' 
        Call the `test_runner` package of the remote repository and parse
        the results.

        Parameters
        ----------

        Returns
        ----------
        `errors` : (`list[str]`)
            List containing potential error strings from the tests
        `failures` : (`list[str]`)
            List containing potential failure strings from the tests
    '''

    cmd = ['python3',"-m", "test_runner"]
    errors, failures = (["UNKNOWN INTERNAL FAILURE"],[])
    try:
        os.chdir(TMP_PATH)
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        print(result.stdout.decode("utf-8"))
        errors, failures = literal_eval(result.stdout.decode("utf-8").splitlines()[-1])
    except Exception as e:
        errors, failures = ([f"INTERNAL FAILURE: {str(e)}"],[])
    finally:
        os.chdir(PROJ_ROOT)
        return errors, failures 

def pull_repo(commit_hash):
    """
        Clones the repository from the remote into a temporary directory.

        Parameters
        ----------
        `commit_hash` : (`str`)
            The sha256 hash of the commit that is to be cloned.
    """

    repo_url = "git@github.com:KTH-DD2480-Fundsoft/assignment-2.git"
    try:
        subprocess.run(["git", "clone", repo_url, TMP_PATH])
        os.chdir(TMP_PATH)
        subprocess.run(["git", "checkout", commit_hash])
    finally:
        os.chdir(PROJ_ROOT)

def remove_repo():
    """
        Removes the repository from the temporary directory.
    """

    subprocess.run(["rm", "-rf", TMP_PATH])
    subprocess.run(["mkdir", TMP_PATH])

