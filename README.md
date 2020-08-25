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
- Windows client requires [the latest version](https://superuser.com/questions/1550291/how-to-install-windows-10-home-19018-update), [WSL 2 Linux kernel](https://docs.microsoft.com/en-gb/windows/wsl/wsl2-kernel) and once Docker is installed [Git](https://git-scm.com/download/win) 

# Local Development

Coalesce is a web application which uses [Django](https://www.djangoproject.com/), [Django Rest Framework](https://www.django-rest-framework.org/), and Postgres on our backend.

For our front end code, we use [Vue.js](https://vuejs.org/)

To start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Documentation

Check out the project's [documentation](http://FederationOfTech.github.io/coalesce/).
