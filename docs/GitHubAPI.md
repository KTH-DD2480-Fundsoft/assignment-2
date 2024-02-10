# GitHub API module documentation

## Description
The CI server utilizes GitHubs API in order to automate certain features and return the CIs evaluation of a certain commit back to GitHub. Currently GitHubs API is utilized in order for the CI server to create commit statuses on the current GitHub commit, that the CI server has just evaluated, which forwards the evaluation status from the CI. All API requests are done with the format *curl* and **do not** utilize GitHubs own client *cli*.

## GitHub Authentication
### GitHub tokens (LINUX systems)
In order to utilize GitHubs API fully and access all aspects of a GitHub repository authentication is required. A simple way to acheive this is to utilize a GitHub token which is passed along with each curl https request. 

Guide to generating a GitHub token: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens 

#### Secure storage of GitHub token
* cd to your home directory on your LINUX os

```
cd
```
* Edit .bash_profile file
```
nano .bash_profile
```
* Add two lines. One for your GitHub username and one for your GitHub token
```
export GitHub_name="NAME"
export GitHub_token="TOKEN"
```
* Save edited .bash_profile file: press "crtl x", followed by "y" and "enter" to save and exit the file

* write cat .bash_profile in terminal to check that your changes were saved

Your GitHub token is now safe and can be accessed by the python library `os` 

### Accessing GitHub tokens from .bash_profile file
The python library `os` can be imported to your python file which will allow you to, among other things, access values stored locally in your os. 

* Import `os`
``` python
import os 
```
* os.environ.get() function gets the value associated with your respective string key

``` python
Github_username = os.environ.get("GitHub_name")
Github_password = os.environ.get("GitHub_token")
```

* `print` allows you to check that the values are correct
```
print("GitHub username: ",Github_username)
print("GitHub password: ",Github_password)
```

## GitHub API

### Using GitHub API with python module requests
In order to create the different https requests that are sent to GitHubs API we use the python library `requests` 

### Currently implemented API functions
We currently utilize one API service for this CI server. The code for the API functions that are utilized by the CI server can be found in the python file "GitHub_API_functions.py". Here is a list of all current GitHub API functions used by the CI server: 
* "Create a commit status": Update status of evaluated commit

### Create a commit status
After the CI tests the pushed commit the ci_logic.py file calls the function `create_commit_status()` from the GitHub_API_functions.py file which updates the commit status of the evaluated commit to either "success", "failure", "error" or "pending" along with a short description of the build status. More info at:
https://docs.github.com/en/rest/repos/webhooks?apiVersion=2022-11-28


