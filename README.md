# arco-react-sample
App for React Development Coding Sample

Simple To-Do List project taken from tutorial found here: https://www.digitalocean.com/community/tutorials/build-a-to-do-application-using-django-and-react

Instructions for Sample Submission

### 
    1. at website https://github.com/arco-data-design/arco-react-sample select 'Use This Template'
    2. follow steps to create your repository on github
    3. clone repository locally (git clone http://github.com/YOU/YOUR_REPO)
    4. move to project directory ('YOUR_REPO')
    5. create and activate python virtual environment using Python 3
        * https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
        * google can help you find alternate instructions for your OS
        * this environment needs to be for python 3.*
    6. install python requirements for the sample:
        * pip install -r backend/requirements.txt
    7. migrate to simple sqlite3 database:
        * python backend/manage.py migrate
    8. run backend server:
        * python backend/manage.py runserver
        * leave this running in a shell window. API calls for the sample will be processed here
        * checkout REST API interface: http://127.0.0.1:8000/api/todos/
    9. frontend setup
        * install yarn (https://classic.yarnpkg.com/en/docs/install)
        * move to arco-react-sample/frontend and run:
            * npm install
        * then run:
            * yarn
        * then run:
            * yarn start
    10. Access the frontend app:
        * http://localhost:3000/
    11. Read the below requirements from the 'client'. Choose a scope that you can think you can complete in 1 hour.
        * the 'clock' starts now - we'll use the honor system, we'd like to know how much quality coding you can accomplish in an hour
        * don't worry if you don't complete everything listed, or if you only focus on a small piece. We understand you have to get oriented first.
        * please don't spend more than 1 hour coding - respect your time :-)
    12. Begin work 
    13. Commit changes with message on your new feature(s)
    14. push commits to your github project, make it public and email the link to contractors@arcodd.com

### Design Requirements
Our "client" would like you to make some updates to our ToDo list application. Please pick some items from the below feature requests that you feel would be the most productive use of your time and complete as much of the work as possible within a 1 hour period. We understand that you may not complete everything in this list - we're looking for high quality, bug free and easily readable work and would prefer to see less items completed well then more attempted and incomplete. Part of this challenge is interpretting non-techincal requests, estimating accurately the time it will take to complete them, and prioritizing effectively - so please don't worry about trying to touch on everything.

In the notes for your commit, please refer to each feature you have completed by letter (A, B, etc) and indicate if you believe the work is complete or incomplete. If incomplete, please give a brief description of your intended next steps. Feel free to include comments in your code detailing this as well.

    A) Display "Due Date" attribute in the list for each todo item
    B) Display "Priority" attribute in the list for each todo item
    C) Include "Due Date" and "Priority" in the edit and create modal, ensure that they can will be entered correctly and provide the user with accurate feedback
    D) Include headers in the list of items
    E) After including headers, ensure that headers stay 'fixed' in the frame when scrolling down through items
    F) highlight rows in red that are past due
    G) update 'completed_time' in the db when marking a todo complete
    H) include orderable column headers - when clicked once, list is now ordered by the attribute corresponding to the header. When click twiced, the header reverses the order
    I) Have the application fill the entire screen
    J) Style the list of Tasks to appear more like a table and include line numbers (1, 2, 3 for each task)
    K) Create new button “all” (next to “complete” / “Incomplete”) and related functionality to display all Tasks
