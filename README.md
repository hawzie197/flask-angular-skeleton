flask/angular4 - skeleton
=========================

installation
============

FOR MAC:

    - install python 3 (https://www.python.org/downloads/)
    - sudo easy_install pip3
    - git clone https://github.com/hawzie197/Flask_Angular4_Skeleton.git
    - cd into Flask_Angular4_Skeleton
    - install virtual environment (for help see section VIRTUALENV MAC)
    - make sure your virtual environment is running.
    - Install all requirements from requirements.txt  'pip install -r requirements.txt'
    - INSTALL NVM (see INSTALL NVM)
    - python manage.py runserver
    - open second terminal
    - cd app/static
    - npm install (get node_modules, could take a while)
    - ng build --dev --watch
    - navigate to: http://127.0.0.1:5000/

FOR WINDOWS:

    - install python 3  'choco install -y python3'
    - install pip  'python -m pip install --upgrade pip'
    - git clone https://github.com/hawzie197/Flask_Angular4_Skeleton.git
    - cd into Flask_Angular4_Skeleton
    - install virtual environment (for help see section VIRTUALENV WINDOWS)
    - make sure your virtual environment is running.
    - install all requirements from requirements.txt  'pip install -r requirements.txt'
    - INSTALL NVM (see INSTALL NVM)
    - python manage.py runserver
    - open second terminal
    - cd app/static
    - npm install (get node_modules, could take a while)
    - ng build --dev --watch
    - navigate to: http://127.0.0.1:5000/


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

INSTALL NVM:
    - curl https://raw.githubusercontent.com/creationix/nvm/v0.25.0/install.sh | bash
    - nvm --version
    - nvm install 6
