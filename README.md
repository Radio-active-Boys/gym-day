# gym-day

# setup virtual env
Windows:
py -m venv gym

Unix/MacOS:
python -m venv gym

# run env
Windows:
gym\Scripts\activate.bat

Unix/MacOS:
source gym/bin/activate

# dependencies
py -m pip install -r requirements.txt

cd GymBackend

# dbms
CREATE DATABASE gym_django
    DEFAULT CHARACTER SET = 'utf8mb4';

# setup mysql root db_name passwd host in setting.py
py manage.py startapp <app_you_want>

# config model of the created app
py manage.py migrate
py manage.py makemigrations

# add user
python manage.py createsuperuser

# run backend
py manage.py runserver
