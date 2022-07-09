# oc-epicevents

OpenClassrooms - P12


## Database Diagram

<img src="./erd.png"/>


## Install & run

Default configuration use a Postgres database.

### Run Postgres with Docker Compose

```shell
docker-compose up
```

### Set environment variable

Refer to your system documentation to define environment variables.
[Linux Environment variable](https://wiki.archlinux.org/title/Environment_variables#Per_user)

```
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=psql_docker
DB_HOST=localhost
DB_PORT=5432
```


