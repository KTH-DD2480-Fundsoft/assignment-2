# Assignment-2 - A Continuous Integration server

This ia a small continuous integration server built using the flask package in Python, GitHub Webhooks, and the GitHub REST API.

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

### Running the server
The server is run with the command
```
pdm run ci-server
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
[File bug in the CI server](FileNotFoundError when running ci_logic.py)
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
