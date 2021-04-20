# Task
The task is to retrieve the commits of all the repositories from amFOSS projects.

## Installation
- I have done this task in a Virtual Environment as some glitches are arising.
- Virtual Environment can be installed by the following command: `sudo apt install virtualenv`
- Make sure a python version >= 3.4 is installed.
- Then I have installed perceval by the following command:
  `$ pip3 install perceval`
  `$pip3 install grimoirelab`
  Pip is a package installer by which perceval can be installed.
 
## Procedure
- Firstly I used request module, which gave me the information about all the amFOSS repositories as a **json** using the API and then I have imported os module which provides functions for intracting with the os.
- Then passed the commnad:  `$ perceval git --json-line https://github.com/amfoss/cms >> commits.json`, which dumped all the commits info inside the commits.json file.
- Then I have provided an interface of python script with the terminal commands. In that, I have used **per_page=100** to get the repos but it can only fetch 100 repos at maximum.

## Result
In the end, 3484 commits were stored in the commits.json file.
