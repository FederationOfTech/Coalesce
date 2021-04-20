# Coalesce

[![Build Status](https://travis-ci.org/FederationOfTech/coalesce.svg?branch=master)](https://travis-ci.org/FederationOfTech/coalesce)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Coalesce is a 100% open-source volunteer management platform.
Its mission is to make recruiting, onboarding, and managing volunteers as easy as possible.
For volunteers, it is made to make finding tasks where you can contribute increadibly simple, allowing you to focus on contributing to the cause that means the most to you.

Coalesce is a [Federation of Humanitarian Technologists](https://federationof.tech) member project.
For more information on the work we do and how to work with us, please see our website.

Some features you can expect from Coalesce are:

 - :mag: Easy browsing of existing volunteer opportunities
 - :loudspeaker: Register new events & recruit volunteers
 - :ballot_box_with_check: Check in volunteers at live events
 - :mage_woman: Generate reports on volunteer activities


# Prerequisites

Docker 
- Available on [Mac](https://docs.docker.com/docker-for-mac/install/) or [Windows](https://docs.docker.com/docker-for-windows/install/) 
- Windows client requires a specific version of [Windows](https://superuser.com/questions/1550291/how-to-install-windows-10-home-19018-update), [WSL 2 Linux kernel](https://docs.microsoft.com/en-gb/windows/wsl/wsl2-kernel) and [Git](https://git-scm.com/download/win). Once up and running Docker can be found on the right of the tool bar. Run `git config core.autocrlf false` before checking out a git branch so that UNIX line-endings needed by containers are used.

# Local Development

Coalesce is a web application which uses [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/), and Postgres on our backend.

For our front end code, we use [Vue.js](https://vuejs.org/)

To start the dev server for local development:
```bash
docker-compose up
```

Once everything is running, you should be able to see:

 - the api server at [http://localhost:8000/](http://localhost:8000/),
 - the frontend at [http://localhost:8080/](http://localhost:8080/),
 - the documentation at [http://localhost:8001/](http://localhost:8001/).

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

# Documentation

Check out the project's [documentation](https://FederationOfTech.github.io/Coalesce/).
