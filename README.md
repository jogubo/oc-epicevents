# oc-epicevents

OpenClassrooms - P12

## Install and run

Default configuration need a Postgres database, you must install it before or change config in `setting.py`.

### Run database with Docker

```shell
docker-compose up
```


### Install and run Django

If you use default config in `setting.py`, you must set environment variable:
- `DB_NAME=postgres`
- `DB_USER=postgres`
- `DB_PASSWORD=psql_docker`
- `DB_HOST=localhost`
- `DB_PORT=5432`

Refer to your system documentation to define environment variables.
[Linux Environment variable](https://wiki.archlinux.org/title/Environment_variables#Per_user)


Create python virtualenv:
```shell
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```shell
pip install -r requierements.txt
```

Make and run migrations:
```shell
python src/manage.py makemigrations
python src/manage.py migrate
```

Create admin:
```shell
python src/manage.py createsuperuser
```

API permissions need groups, you can create `Manager`, `Salesman` and `Support`
easily with:
```shell
python src/manage.py creategroups
```

Run Django:
```
python src/manage.py runserver
```

## Database Diagram

<img src="./erd.png"/>


## Groups Permissions


### Manager

- Can read, create, update and destroy `User` with django admin
- Can read, create, update and destroy `Client` with django admin or API
- Can read, create, update and destroy `Contract` with django admin or API
- Can read, create, update and destroy `Event` with django admin or API


### Salesman

- Can read, create and update `Client` with API
- Can read, create and update `Contract` with API
- Can read and create `Event` with API

*Can update only if user is sales contact.*


### Suport

- Can read `Client` with API
- Can read and update `Event` with API

*Can update only if user is support contact and event date has not passed.*
