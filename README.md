flask/angular4 - skeleton
=========================

installation
============

FOR MAC:

    - install python 3 (https://www.python.org/downloads/)
    - sudo easy_install pip3
    - create directory (PROJECT NAME)
    - cd into project
    - install virtual environment (for help see section VIRTUALENV MAC)
    - Install all requirements from requirements.txt  'pip install -r requirements.txt'
    - python manage.py runserver
    - open second terminal
    - cd app/static
    - ng build --dev --watch


FOR WINDOWS:

    - install python 3  'choco install -y python3'
    - install pip  'python -m pip install --upgrade pip'
    - create directory (PROJECT NAME)
    - cd into project
    - install virtual environment (for help see section VIRTUALENV WINDOWS)
    - Install all requirements from requirements.txt  'pip install -r requirements.txt'
    - python manage.py runserver
    - open second terminal
    - cd app/static
    - ng build --dev --watch


CHECK PYTHON VERSION:

    - python -V ( > 3.4 )

VIRTUALENV MAC:

    - pip install virtualenv
    - run: virtualenv env
    - activate: source env/bin/activate

VIRTUALENV WINDOWS:

    - pip install virtualenv
    - run virtualenv env
    - cd env/Scripts/activate

