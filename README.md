# GraphQL Programming Assignment
A web application written using the Django framework that allows a user to query the Countries GraphQL API (https://github.com/trevorblades/countries), written during the recruitment process of a software engineering role.

To deploy the application locally on a Django development server, accessible by default at localhost:8000, the following steps need to be taken on a machine with a valid Python 3 installation:
1. Clone the repository from https://github.com/nt294/GraphQL_Programming_Assignment
2. Navigate to the directory containing the ‘manage.py’ file and run the following commands:

(Recommended to create and activate a Python virtual environment first)
* $ pip install -r requirements.txt
* $ python manage.py makemigrations
* $ python manage.py migrate
* $ python manage.py runserver
