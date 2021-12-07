echo Starting server
python3 ./app/manage.py migrate
python3 ./app/manage.py createsuperuser
python3 ./app/manage.py runserver 0.0.0.0:80