# yamdb_final
[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
![example workflow](https://github.com/xewus/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


The "Yamdb" project collects user reviews of various works,
such as: books, songs, paintings etc.


# Technologies:

- Python
- Django
- Nginx
- Postgress
- Docker

# How to use it:

- Upload from yamdb/infra/ the file "docker-compose.yaml" and the folder "nginx/" to your server.
- Create the file ".env" like it:
```
SECRET_KEY='<Your secret key for Django app>'
HOSTS='<Your host>'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<your password for database>
DB_HOST=db
DB_PORT=5432
```

Install docker on your server:
```
sudo apt install docker.io
```
Install Docker Compose (for Linux):
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Get permissions for docker-compose:
```
sudo chmod +x /usr/local/bin/docker-compose
```
Pull and run docker containers:
```
sudo docker-compose up
```
Create superuser:
```
docker-compose exec web python manage.py createsuperuser
```
Look the available resources:
```
http://<your host>/redoc
```