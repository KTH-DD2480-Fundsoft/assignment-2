from ci_server import log, github_owner, github_repo, github_token
import requests
from requests.auth import HTTPBasicAuth
import os


'''
GitHub_API_functions.py includes the different API requests that the CI server does. It utilizes the python library 'requests' to simply the 
curl https requests
'''

import requests
from requests.auth import HTTPBasicAuth
import os



def create_commit_status(commit_hash, status):
  '''
    Creates a POST request to the GitHub repository in order to update the
    status of the commit identified by `commit_hash`, namely the commit
    that was recently evaluated on the CI server. Updates the commit status
    of the commit on GitHub from the CI server through the GitHub API. Also
    adds a description and context string from the CI that adds additional
    information from the CI regarding the build.

    Parameters
    ----------
    `commit_hash` : (`str`)
      The sha256 hash of the commit whose commit status is to be updated.
    `status` : (`str`)
      The status of the evaluation of the commit build. Can be either "success", "failure", "error" or "pending".

    Returns
    ----------
    `returned_status_code` : (`int`)
      The status code of the POST request. `201` if the update could be made.
    `returned_set_state` : (`str`)
      The echoed state of the commit status from the POST request, or a message if `returned_status_code` is not `201`.
  '''

  # GitHub parameters
  OWNER, REPO = github_owner, github_repo
  SHA  = commit_hash

  # Data about the commit to post on GitHub
  if status == "success":  
    COMMIT_DESCRIPTION = "The build succeded!"
    CONTEXT = "Continuos integration server"
  elif status == "failure":
    COMMIT_DESCRIPTION = "The build failed!"
    CONTEXT = "Continuos integration server"
  elif status == "error":
    COMMIT_DESCRIPTION = "The build encountered an error!"
    CONTEXT = "Continuos integration server"
  elif status == "pending":
    COMMIT_DESCRIPTION = "The build is pending!"
    CONTEXT = "Continuos integration server"
  else: raise ValueError("invalid status")

  # Create commit status
  url_commit = f"https://api.github.com/repos/{OWNER}/{REPO}/statuses/{SHA}"
  data = {"state":status,"target_url":"https://prompt-possum-first.ngrok-free.app/","description":COMMIT_DESCRIPTION,"context":CONTEXT}

  headers = {'Authorization': 'token ' + github_token}

  # Create and send POST request
  post_response = requests.post(url_commit
                                ,json=data
                                ,headers=headers)
  # returns status code and state that was set/potential error message from POST request response
  returned_status_code = post_response.status_code
  log.info(f"API response headers: {post_response.headers}")
  if post_response.status_code == 201:
    log.info("successfully set commit status")
    returned_set_state   = post_response.json()["state"]
    returned_target_url  = post_response.json()["target_url"]
  else:
    returned_set_state   = post_response.json()["message"]
    returned_target_url    = "Fail"

  return returned_status_code, returned_set_state, returned_target_url

