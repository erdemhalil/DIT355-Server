# Server

The server is the software that interfaces with the database. The server communicates to provide and exchange data that is requested. 

## Setup Instructions

### Prerequisites 

To run the server you will need Python 3.9 or later, pip and PostgreSQL installed on your computer.

You can install them by clicking on the according option below (you'll be redirected to a third-party web page):
- [Python & pip](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

### Running

1. Launch a terminal, navigate to the server folder by using the commands from the root directory: 

    `cd .\server\server`

2.To get the server running you need to create an environment for python, this can be done by these following commands for your given system:

**MacOS:**
    `python -m venv env` &&
    `source env/bin/activate`

**Windows:**
    `python -m venv env` &&
    `.\venv\Scripts\activate`

3. Install the required requirements using the command: 

    `pip install -r requirements.txt`

4. Setup the database using the following commands: 

    `python3 manage.py makemigrations`  
    `python3 manage.py migrate` 

NOTE: In case the commands do not run, try running them the simpler `python` command (instead of `python3`): 

5. You can now start the server by running the following command:

    `python3 manage.py runserver`

By default, it will use port 8000 on your localhost. 
