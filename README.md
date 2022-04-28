# POKEMON

## This is a Django REST Framework project, where I created an API for pokemon, which maintains the basic functionalities involving CRUD

### Installing and setting up
* Clone the repo in your local directory
* Create a virtual env (here named as .venv) in your local directory 
```
python -m venv .venv
```
* Activate the virtual env with (if in windows):
```
.venv\Scripts\activate
```
* Then install all the requirements using pip command
```
 pip install -r requirements.txt
```

* Now make any migrations if needed using
```
python manage.py makemigrations
python manage.py migrate
```
* Create a superuser using:(if you want to make/see changes from the admin portion of django)
```
python manage.py createsuperuser
```

### Using the API:
* Using your browser or postman, visit and implement the CRUD functions
* OR, run:
```
python consum.py
```
to GET all the objects from the API. Change/Edit the consume.py file to play with the API
