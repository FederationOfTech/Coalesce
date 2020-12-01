# coalesce

[![Build Status](https://travis-ci.org/FederationOfTech/coalesce.svg?branch=master)](https://travis-ci.org/FederationOfTech/coalesce)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

An open source volunteer management platform. Check out the project's [documentation](https://FederationOfTech.github.io/Coalesce/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Start the dev server for local development:

```bash
docker-compose up
```

Once everything is running, you should be able to see:

 - the api server at [http://localhost:8000/](http://localhost:8000/),
 - the frontend at [http://localhost:8080/](http://localhost:8080/),
 - the documentation at [http://localhost:8001/](http://localhost:8001/).

Create a superuser to login to the admin:

```bash
docker-compose exec api ./manage.py createsuperuser
```

Run a command inside the api backend docker container:

```bash
docker-compose exec api [command]
```

For example, `[command]` can be `/bin/bash` and you get a shell to the running container.

Once you are in the container, you can then run the tests by doing:

```bash
./manage.py test
```

You can also start the django shell by doing:

```bash
./manage.py shell
```

To connect to the postgresql database, you can either do:

```bash
docker-compose exec postgres psql -U postgres
```

or connect to `localhost` on port `5432` using a local postgresql client.
