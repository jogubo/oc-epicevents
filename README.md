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


# API Documentatin

## Login User
### Method: POST
>```
>http://127.0.01:8000/api/token/
>```
### Body (**raw**)

```json
{
    "email": "{{userLogin}}",
    "password": "{{userPassword}}"
}
```

### Response: 200
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzkwMTQxMywiaWF0IjoxNjU3ODE1MDEzLCJqdGkiOiJjZjc0M2U0OTg1YTc0Njc0OTQ5ODk0MWNhNDVjODBjOCIsInVzZXJfaWQiOjJ9.hSTLG1N9Jso6HbgzKv14lj6xnzOVhTeQaLmVyDsjJnQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3ODE1MzEzLCJpYXQiOjE2NTc4MTUwMTMsImp0aSI6IjZjNmU3OTk1ZTZmOTQ4NmI4MzQ0NTc2ZDNjZTY4MTM1IiwidXNlcl9pZCI6Mn0.KW0OFFlcobTe0nDZe87CHI5SppVSzNpsFYBy2N77cMU"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Refresh Token
### Method: POST
>```
>http://127.0.01:8000/api/token/refresh/
>```
### Body (**raw**)

```json
{
    "refresh": "{{refreshToken}}"
}
```

### Response: 200
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3ODE1MzM4LCJpYXQiOjE2NTc4MTUwMTMsImp0aSI6ImU0YjNlMGY5ZmNmNjRmMGE4OGZjZWQxMzkwMjVmY2FhIiwidXNlcl9pZCI6Mn0.aa4JAzqJS52w7b3gCOBCnj6aeKQKeeDgxpUXq09XewE"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Clients List
### Method: GET
>```
>http://127.0.0.1:8000/api/clients/?first_name=&last_name&email&phone&mobile&compagny_name
>```
### Query Params

|Param|value|
|---|---|
|first_name||
|last_name|null|
|email|null|
|phone|null|
|mobile|null|
|compagny_name|null|


### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "first_name": "First Name 1",
            "last_name": "Last Name 1",
            "email": "client@1.mail",
            "phone": "0100000000",
            "mobile": "0600000000",
            "compagny_name": "Compagny 1",
            "date_created": "2022-07-14T16:07:53.303690Z",
            "date_updated": "2022-07-14T16:07:53.303700Z",
            "sales_contact": 2,
            "is_client": false
        },
        {
            "id": 2,
            "first_name": "First Name 2",
            "last_name": "Last Name 2",
            "email": "client@2.mail",
            "phone": "0100000000",
            "mobile": "0600000000",
            "compagny_name": "Compagny 2",
            "date_created": "2022-07-14T16:09:00.178000Z",
            "date_updated": "2022-07-14T16:09:00.178009Z",
            "sales_contact": 2,
            "is_client": false
        },
        {
            "id": 3,
            "first_name": "First Name 3",
            "last_name": "Last Name 3",
            "email": "client@3.mail",
            "phone": "0100000000",
            "mobile": "0600000000",
            "compagny_name": "Compagny 3",
            "date_created": "2022-07-14T16:09:58.722937Z",
            "date_updated": "2022-07-14T16:09:58.722946Z",
            "sales_contact": 2,
            "is_client": false
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Create Client
### Method: POST
>```
>http://127.0.0.1:8000/api/clients/
>```
### Body (**raw**)

```json
{
    "first_name": "Client First Name",
    "last_name": "Client Last Name",
    "email": "client@email.com",
    "phone": "0100000000",
    "mobile": "0600000000",
    "compagny_name": "Compagny Name",
    "sales_contact": 2
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 4,
    "first_name": "Client First Name",
    "last_name": "Client Last Name",
    "email": "client@email.com",
    "phone": "0100000000",
    "mobile": "0600000000",
    "compagny_name": "Compagny Name",
    "date_created": "2022-07-14T16:16:12.941317Z",
    "date_updated": "2022-07-14T16:16:12.957639Z",
    "sales_contact": 2,
    "is_client": false
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Client
### Method: GET
>```
>http://127.0.0.1:8000/api/clients/{{clientID}}/
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "first_name": "First Name 1",
    "last_name": "Last Name 1",
    "email": "client@1.mail",
    "phone": "0100000000",
    "mobile": "0600000000",
    "compagny_name": "Compagny 1",
    "date_created": "2022-07-14T16:07:53.303690Z",
    "date_updated": "2022-07-14T16:07:53.303700Z",
    "sales_contact": 2,
    "is_client": false
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Update Client
### Method: PUT
>```
>http://127.0.0.1:8000/api/clients/{{clientID}}/
>```
### Body (**raw**)

```json
{
    "first_name": "Edit Client First Name",
    "last_name": "Edit Client Last Name",
    "email": "client@email.com",
    "phone": "0100000000",
    "mobile": "0600000000",
    "compagny_name": "Edit Compagny Name",
    "sales_contact": 2
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 4,
    "first_name": "Edit Client First Name",
    "last_name": "Edit Client Last Name",
    "email": "client@email.com",
    "phone": "0100000000",
    "mobile": "0600000000",
    "compagny_name": "Edit Compagny Name",
    "date_created": "2022-07-14T16:16:12.941317Z",
    "date_updated": "2022-07-14T16:22:14.596113Z",
    "sales_contact": 2,
    "is_client": false
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Delete Client
### Method: DELETE
>```
>http://127.0.0.1:8000/api/clients/{{clientID}}/
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Contracts List
### Method: GET
>```
>http://127.0.0.1:8000/api/contracts/?sales_contact=&client&status=&amount&payment_due
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|sales_contact||
|client|null|
|status||
|amount|null|
|payment_due|null|


### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "sales_contact": 2,
            "client": 1,
            "date_created": "2022-07-18T09:44:38.222596Z",
            "date_updated": "2022-07-18T09:44:38.222604Z",
            "status": true,
            "amount": 100,
            "payment_due": "2023-07-18T10:00:00Z"
        },
        {
            "id": 2,
            "sales_contact": 2,
            "client": 1,
            "date_created": "2022-07-19T12:38:57.032136Z",
            "date_updated": "2022-07-19T12:38:57.032144Z",
            "status": false,
            "amount": 300,
            "payment_due": "2024-09-19T10:00:00Z"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Create Contract
### Method: POST
>```
>http://127.0.0.1:8000/api/contracts/
>```
### Body (**raw**)

```json
{
    "sales_contact": 2,
    "client": 1,
    "status": false,
    "amount": 100,
    "payment_due": "2023-09-18T10:00:00Z"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 3,
    "sales_contact": 2,
    "client": 1,
    "date_created": "2022-07-19T12:55:07.035328Z",
    "date_updated": "2022-07-19T12:55:07.048321Z",
    "status": false,
    "amount": 100,
    "payment_due": "2023-09-18T10:00:00Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Contract
### Method: GET
>```
>http://127.0.0.1:8000/api/contracts/{{contractID}}
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "sales_contact": 2,
    "client": 1,
    "date_created": "2022-07-18T09:44:38.222596Z",
    "date_updated": "2022-07-18T09:44:38.222604Z",
    "status": true,
    "amount": 100,
    "payment_due": "2023-07-18T10:00:00Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Update Contract
### Method: PUT
>```
>http://127.0.0.1:8000/api/contracts/{{contractID}}/
>```
### Body (**raw**)

```json
{
    "sales_contact": 2,
    "client": 1,
    "status": true,
    "amount": 100,
    "payment_due": "2023-09-18T10:00:00Z"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 3,
    "sales_contact": 2,
    "client": 1,
    "date_created": "2022-07-19T12:55:07.035328Z",
    "date_updated": "2022-07-19T13:00:34.294559Z",
    "status": true,
    "amount": 100,
    "payment_due": "2023-09-18T10:00:00Z"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Delete Contract
### Method: DELETE
>```
>http://127.0.0.1:8000/api/contracts/{{contractID}}/
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Events List
### Method: GET
>```
>http://127.0.0.1:8000/api/events?client&support_contact&attendees&event_date&note
>```
### Body (**raw**)

```json

```

### Query Params

|Param|value|
|---|---|
|client|null|
|support_contact|null|
|attendees|null|
|event_date|null|
|note|null|


### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "client": 1,
            "date_created": "2022-07-18T09:47:39.311014Z",
            "date_updated": "2022-07-18T09:47:39.311022Z",
            "support_contact": 4,
            "attendees": 3,
            "event_date": "2022-04-10T18:00:00Z",
            "note": "Note"
        },
        {
            "id": 2,
            "client": 1,
            "date_created": "2022-07-19T13:07:19.072393Z",
            "date_updated": "2022-07-19T13:07:19.072400Z",
            "support_contact": 4,
            "attendees": 6,
            "event_date": "2022-07-19T17:00:00Z",
            "note": "None"
        }
    ]
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Create Event
### Method: POST
>```
>http://127.0.0.1:8000/api/events/
>```
### Body (**raw**)

```json
{
    "client": 1,
    "support_contact": 4,
    "attendees": 3,
    "event_date": "2022-04-10T18:00:00Z",
    "note": "Note"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 201
```json
{
    "id": 3,
    "client": 1,
    "date_created": "2022-07-19T13:16:22.267482Z",
    "date_updated": "2022-07-19T13:16:22.280635Z",
    "support_contact": 4,
    "attendees": 3,
    "event_date": "2022-04-10T18:00:00Z",
    "note": "Note"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Get Event
### Method: GET
>```
>http://127.0.0.1:8000/api/events/{{eventID}}
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 1,
    "client": 1,
    "date_created": "2022-07-18T09:47:39.311014Z",
    "date_updated": "2022-07-18T09:47:39.311022Z",
    "support_contact": 4,
    "attendees": 3,
    "event_date": "2022-04-10T18:00:00Z",
    "note": "Note"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Update Event
### Method: PUT
>```
>http://127.0.0.1:8000/api/events/{{eventID}}/
>```
### Body (**raw**)

```json
{
    "client": 1,
    "support_contact": 4,
    "attendees": 3,
    "event_date": "2022-04-12T18:00:00Z",
    "note": "Note"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 200
```json
{
    "id": 3,
    "client": 1,
    "date_created": "2022-07-19T13:16:22.267482Z",
    "date_updated": "2022-07-19T13:18:04.241614Z",
    "support_contact": 4,
    "attendees": 3,
    "event_date": "2022-04-12T18:00:00Z",
    "note": "Note"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## Delete Event
### Method: DELETE
>```
>http://127.0.0.1:8000/api/events/{{eventID}}/
>```
### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{accessToken}}|string|


### Response: 204
```json
null
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
