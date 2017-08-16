Flask/Angular 4 - Skeleton
=========================

One thing to note is that flask calls Angular's index.html file located 'static/src/index.html' which serves
the angular app. It is important to note that flask finds the index.html upon building in the 'dist' directory.

Another note is that an efficient way to develop the angular flask app is to use two different terminals.
One terminal will run the server side. (to run server side: python manage.py runserver)
The second terminal will run the client side. (ng build --dev --watch)

============
Requirements
============

- python 3
- pip
- nvm (node version manager)
- npm > 3
- node > 5
- angular cli
- virtualenv

Install Python 3:

- https://www.python.org/downloads/
- python -v ( > 3.4 )

Install pip (MAC):

- sudo easy_install pip3

Install pip (WINDOWS):

- python -m pip install --upgrade pip

Install nvm (MAC):

- curl https://raw.githubusercontent.com/creationix/nvm/v0.25.0/install.sh | bash
- close terminal and reopen
- nvm --version

Install nvm (WINDOWS):

- https://github.com/coreybutler/nvm-windows/releases
- close terminal and reopen
- nvm --version

Install node and npm (with nvm):

- nvm install 6
- npm -v
- node -v

Install Angular CLI:

- npm install -g @angular/cli
- ng -v

Install virtualenv:

- pip install virtualenv

============
Setup
============

1. open terminal
2. cd desktop
3. create directory EX. fl_angular4
4. cd into that directory
5. git clone https://github.com/hawzie197/Flask_Angular4_Skeleton.git
6. cd into Flask_Angular4_Skeleton
7. run create virtual env (see below for mac vs windows)
8. pip install -r requirements.txt
9. python manage.py runserver
10. open second terminal
11. cd app/static
12. check node/npm versions (if not correct, run: nvm use 6) # import because of angular's package-lock.json
13. npm install (get node_modules, could take a while)
14. ng build --dev --watch
15. navigate to: http://127.0.0.1:5000/

VIRTUALENV MAC:

    - run: virtualenv env
    - activate: source env/bin/activate

VIRTUALENV WINDOWS:

    - run virtualenv env
    - cd env/Scripts
    - activate
