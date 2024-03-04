This is a simple example in Django.

To start the project you need to:
- create your virtual environment inside the project directory: python3 -m venv venv (python -m venv venv for Windows)
- activate the virtual envoronment: source venv/bin/activate (venv\Scripts\activate for Windows)
- install necessary modules: pip install -r requirements.txt
- execute DB migrations: python manage.py migrate
- start webserver: python manage.py runserver
