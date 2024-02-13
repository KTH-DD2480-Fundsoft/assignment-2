# Assignment-2 - A Continuous Integration server

This is a small continuous integration server built using the Flask package in Python, GitHub Webhooks, and the GitHub REST API. The list of past builds can be found at https://prompt-possum-first.ngrok-free.app/

## Instructions for running
[PDM](https://pypi.org/project/pdm/) is required for running the server and the server tests. [PDM](https://pypi.org/project/pdm/) can be installed via `pip` with the command 

```
pip install pdm
```

Other ways of installing PDM can be found at 
https://pypi.org/project/pdm/ 

### Running tests
Once PDM is configured, the tests are run with the command
```
pdm run test
```

The tests are implemented using the unittest module in python. The package compileAll is used to do the static syntax check of all files related to the server. Additionally, there are tests for continuous integration, GitHub REST API, logger, and for the Flask server. These can all be found in test_ci_server.

### Running the server
A dev server can be run using
```
pdm run dev-server
```

and a prod server can be run using

```
pdm run prod-server
```

Ngrok is used for tunnelling the traffic between our [domain](https://prompt-possum-first.ngrok-free.app/) and the server running on KTH's server. This tunnelling is set up with the command

```
pdm run ngrok
```
 
### Generating the documentation
The documentation is generated with the command
```
pdm run docs
```

and can then be seen by opening `docs/build/html/index.html` in a web browser.

## Structure
The repo itself will be structured in the following way:

```
.
├── ci-server
│   └── where we put the source for the CI-server itself 
├── docs
│   └── where we put all the documentation 
├── log
│   └── where we put all logs (will contain old build data)
├── main.py
├── README.md
├── test_ci-server
│   └── where we put all the tests of the CI-server
└── tmp
    └── where we clone the repo to be CI:d 

```

The server will be run at KTH student-shell2, using ngrok to tunnel past
KTH firewall. The whole program will be structured something like this:
![Failed to load file!](docs/img/structure.png)

We will inform CI failure/success through the use of GitHub build Status
via the GH REST API. We will create a simple web interface were build 
history can be viewed.

## Contributing / Workflow
We use a GitHub organization to track our development process, creating a project
to make use of Github's Kanban-like issue board and link this repository to said 
project. 

Thoroughly develop the backlog before starting to work on tickets.
Tickets are connected to specific branches that implement the tickets, these are
merged into our main branch through pull-requests.

### TBD - Trunk-based development
We used a trunk-based development model in which we, for each feature, bug, docs, etc,
create branches of the main branch indicating atomic changes relating to a specific
ticket. 

These branches *need* to be connected to an actual issue. For example, if I want
to add a feature, I create a branch titled feature/[ISSUE NUMBER]/name-of-feature.

Branches are merged to the main only through the use of GitHub pull requests.

### Conventional Commits
We used the format "conventional commits" in or commit messages. Every commit has the 
the following format (bar merge commits and conflict resolutions):

```
<type>(<optional scope>)<!>: <description>
<BLANK LINE>
<optional body>
<BLANK LINE>
<optional footer(s)>
```

### Releases
We do a trunk based release. Where we simply branch of the main branch into a release 
branch named `release/x.x.x`, tag it `x.x.x`, and possibly make a GH Release. Whether
we can make the server self-update on a specific release webhook is to be investigated.


### Squash and merge!
Always use the "squash and merge" option when merging GitHub PRs.

### Commit status notification and unit testing
Our implementation of commit status notifications includes using GitHubs API to update the commit status of a certain commit. This was implemented by using the python library `requests` which simplified the curl POST request needed for the API. More specifically the CI server that we've built tests and evaluates each commit that is pushed to GitHub. The CI server evaluates the commit and returns "success" if all tests pass and "failure" or "error" depending on if the tests fail or if an error occurs respectively. This status is then passed on along with the hash of that commit to the function "create_commit_status" which uses the request library in order to create a POST request to GitHubs API. The POST request includes the status of the commit (if the commit passed the tests or not), a description of how the build went, along with a target url which links that commit to our CI server. The target url link allows a user to be rerouted to our CI servers webpage where more information can be found such as build histories. Thus the resulting commit on GitHub recieves a status of how the build tests went which is displayed graphically on the commit. Making it very clear how the commit has performed and if it is ready to be merged or not.

When unit testing this function we tested that all the different commit statuses could be set, that the function returns correct error messages and that the target url that links to our CI server works. This was done with 6 unit tests where the first 4 simply conducted one POST request each which tested setting the commits status to "succes", "failure", "error" or "pending". These tests also checked so that the returned values that the GitHub API returns are correct and match the values from the CI server. The fifth test checks how the function handles errors that can occur if the wrong commit hash or value is sent with the POST request. If this happens then the GitHub API returns an error json file where values can be extracted and returned in order to highlight what went wrong. The sixth and final test checks that the target url of the commit, which links it to our CI server, is correctly implemented in GitHub. All unit tests utilized the python library `unittest` and different assert functions to validate the output. 

### Essence state
We are currently in the "In place" state of the Essence heirarchy. In the last assignment we said that we were in the "In use" state as we had only established how we wanted to work. As GitHub and a more structured way of working was new for some group members they had not fully adapted to and become used to the workflow of a larger group project. This has however changed for assignment 2 where all team members are now accustomed to the workflow where commit messages syntax, pull requests, solving merge conflicts and other workflow tools are now well established and work well. Thus all group members now work within the same workflow autonomously. This frees up time and effort to solely focus on the issues and on solving the assignment. With regard to this some ideas as to improve the workflow are still being made even if these constitute minor changes addressing minor inefficiencies. An example of this being how we approve and squash merge pull requests. Team wise we'd say that we are currently in the "collaborating" phase where all team members are working comfortably together as a unit. In order to further improve and achieve the next steps "Working well" and "performing" when it comes to workflow and team functionality we need to continue with what we're doing (in order to further establish our workflow) and focus on evaluating each assignment with constructive feedback to address issues and actively work on being a more effective team.

# Statement of contributions

## Review process 
Using Github pull requests, we made sure that every group member got to write issues,
create pull requests, review pull requests, and write code (resolving issues). This 
was done in an ad-hoc manner.

## Rasmus Danielsson
### Issues 
[Global logger](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/56)
[Release preparations](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/51)
[Test wrapper](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/43)
[AUTH_KEY bug](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/40)
[Connection between CI and Github API](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/31)
[Figure out server testing](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/21)
[Implementation of webhooks](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/15)
[Flask server skeleton](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/6)
[Logger interface and structure](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/5)
[Draft of project structure](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/1)


## Dante Astorga Castillo
### Issues
[Documentation of API functions](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/45)
[Bug in the CI server](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/32)
[File bug in the CI server](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/32)
[Package management for the CI server](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/13)


## Sebastian Montén
### Issues
[Fix the server tests after authentication change](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/52)
[Webhook bug](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/40)
[Unique URL for each build](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/27)
[Compilation tests](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/23)
[Extension of logging to builds](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/16)
[Implementation of webhooks](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/15)
[Investigation into webhooks](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/2)

## Ludvig Skare
### Issues
[Add info about notificiations](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/59)
[Set up correct link for commit statuses](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/54)
[Remove print to stdout in compilation tests](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/53)
[Documentation of API functions](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues?q=is%3Aissue+assignee%3Alskare)
[Add ESSENCE standard to README](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/45)
[Investigate Github REST API](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/3)

## Victor Stenmark
### Issues
[Parts of README](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/60)
[Documentation of API functions](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/45)
[URL indexing for past builds](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/39)
[Documentation bug](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/24)
[Investigate web interface for builds](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/22)
[Logic for the CI server](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/11)
[Test structure for the CI server](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/7)
[Documentation setup](https://github.com/KTH-DD2480-Fundsoft/assignment-2/issues/4)
