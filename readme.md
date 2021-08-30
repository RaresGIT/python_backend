#### How to run locally

Windows:

```sh
    #make sure you are in the base folder
    pipenv shell
    #if the env is not setup, do:
    pipenv install

    # then finally run the server
    python manage.py runserver


```

Linux:

```sh
    # make sure you are in the base folder
    pipenv shell
    # if the env is not setup, do:
    pipenv install

    # then finally run the server
    python manage.py runserver
```

#### Start Postgresql Service

```sh
    sudo service postgresql start
```

#### Navigate PSQL ENV

In order to run these migrations, we're using PostgreSQL, ran in a Linux Env.

The following commands might be useful:

```sh
    Access DB shell:
    psql <db_name>

    Here you can right any SQL commands to debug DB
```

```sh
    Some other PSQL useful shortcuts:

    List all tables:
    \d


```

#### Migrate and upgrade DB

If you make any changes to the structure of the ORM, you will need to migrate and upgrade the DB. If you are running the app for the first time please also run the init command (you should have a migrations directory inside of the api directory).

Before trying to run any db commands, make sure postgresql is running locally as a service.
Follow the steps at <http://postgresguide.com/setup/install.html> for installation guide.

Init DB:

```sh
    python manage.py db init
```

Migrate ORM: (update any changes)

```sh
    python manage.py db migrate
```

Upgrade ORM: (update the local migrations)

```sh
    python manage.py db upgrade
```

#### ENDPOINTS:

# needs to be updated!!!

| Verb   | Endpoint URI   | Description                                           |
| ------ | -------------- | ----------------------------------------------------- |
| (GET)  | /              | -> home url                                           |
| (POST) | /register      | -> register a user to be able to access the endpoints |
| (POST) | /login         | -> login using the credentials registered             |
| (GET)  | /groups        | -> fetch all groups                                   |
| (POST) | /create_groups | -> create a new group                                 |
