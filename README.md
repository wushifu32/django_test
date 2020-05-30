Run this web:
* Install django
``` bash
# Set a python virtual vironment
python3 -m venv ~/.virtualenvs/djangodev
source ~/.virtualenvs/djangodev/bin/activate
# Install django
pip3 install Django
```
* Clone or download this repo
* Start web
```bash
python3 manage.py runserver --insecure
```

Run test:
```bash
python3 manage.py test polls
```

Run on nginx server:
* Install nginx & uwsgi
```bash
sudo install nginx
pip3 install uwsgi
```
* Amend the path in django_nginx.conf & uwsgi.ini
* Start web
```bash
sudo ln -s ./django_nginx.conf /etc/nginx/sites-enabled/
python3 manage.py collectstatic
#uwsgi --ini ./uwsgi.ini --uid www-data --gid www-data
uwsgi --ini ./uwsgi.ini
sudo server nginx start
```
