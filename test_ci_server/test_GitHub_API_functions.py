import unittest
from ci_server.GitHub_API_functions import create_commit_status


class TestGitHubAPIFunctions(unittest.TestCase):
    '''
        Class containing tests for `ci_server/GitHub_API_functions.py` which interfaces
        with GitHub's REST API.
    '''

    def test_commit_status_success(self):
        '''
            Tests that the status of the initial commit can be set to "success".
        '''

        # Commit hash corresponds to "Intial commit" in assignment 2 repository
        commit_hash = "00ba07dbe885385f308741a4bc70e1c866f2da7f"
        status = "success"
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 201) # Checks that the POST request was successful in updating commit status
        self.assertEqual(returned_set_state, status) # Check that the POST request set the right commit status

    def test_commit_status_failure(self):
        '''
            Tests that the status of the initial commit can be set to "failure".
        '''

        # Commit hash corresponds to "Intial commit" in assignment 2 repository
        commit_hash = "00ba07dbe885385f308741a4bc70e1c866f2da7f"
        status = "failure"
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 201) # Checks that the POST request was successful in updating commit status
        self.assertEqual(returned_set_state, status) # Check that the POST request set the right commit status

    def test_commit_status_error(self):
        '''
            Tests that the status of the initial commit can be set to "error".
        '''

        # Commit hash corresponds to "Intial commit" in assignment 2 repository
        commit_hash = "00ba07dbe885385f308741a4bc70e1c866f2da7f"
        status = "error"
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 201) # Checks that the POST request was successful in updating commit status
        self.assertEqual(returned_set_state, status) # Check that the POST request set the right commit status
    
    def test_commit_status_pending(self):
        '''
            Tests that the status of the initial commit can be set to "pending".
        '''

        # Commit hash corresponds to "Intial commit" in assignment 2 repository
        commit_hash = "00ba07dbe885385f308741a4bc70e1c866f2da7f"
        status = "pending"
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 201) # Checks that the POST request was successful in updating commit status
        self.assertEqual(returned_set_state, status) # Check that the POST request set the right commit status
    
    def test_error_handling(self):
        '''
            Tests that the status of a non-existing commit cannot be changed and that the correct
            error message is returned.
        '''

        commit_hash = "40"
        status = "pending"
        error_message = 'No commit found for SHA: 40'
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 422) # Checks that the POST request was not successful in updating commit status
        self.assertEqual(returned_set_state, error_message) # Check that the error message is as expected
        self.assertEqual(returned_target_url,"Fail") # Checks that the echoed target url is as expected

    def test_ngrok_server_github_connection(self):
        # Commit hash corresponds to "Intial commit" in assignment 2 repository
        commit_hash = "00ba07dbe885385f308741a4bc70e1c866f2da7f"
        status = "success"
        returned_status_code, returned_set_state, returned_target_url = create_commit_status(commit_hash, status)
        self.assertEqual(returned_status_code, 201) # Checks that the POST request was successful in updating commit status
        self.assertEqual(returned_target_url, "https://prompt-possum-first.ngrok-free.app/") # Checks that the echoed target url is as expected


if __name__ == '__main__':
    unittest.main()