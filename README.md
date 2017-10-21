# Regio Helden Django Challenge #

[![Build Status](https://api.travis-ci.org/rexhepberlajolli/RHChallenge.svg?branch=master)](https://travis-ci.org/rexhepberlajolli/RHChallenge)

This is the django challenge for [Regio Helden GMBH](https://www.regiohelden.de/)

## Dependencies
- [Docker Community Edition](https://www.docker.com/community-edition)

## Technologies 
- [Python 3.6](https://www.python.org/downloads/)
- [Django 1.11.6](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Install
To build this project you need to have docker installed on your machine.

- Git clone the project
``` 
    $ git clone https://github.com/rexhepberlajolli/RHChallenge.git
``` 
- Build docker image
``` 
    $ docker-compose build
``` 
- Apply migrations to the database
```
    $ docker-compose run web python -u /opt/webapp/manage.py migrate
```
- Run docker containers
```
    $ docker-compose up
```
- Navigate to following url in your browser to check out the application
```
    http://127.0.0.1
```

## Tests
- Run the tests using the following command
```
    $ docker-compose run web python manage.py test
```
## Tests Code Coverage
- Run the tests with code coverage using the following commands
```
    $ docker-compose run web coverage run ./manage.py test user_administration
    $ docker-compose run web coverage report
```
- Or for a nicer coverage report use the following command then open htmlcov/index.html in the browser
```
    $ docker-compose run web coverage report html
```

## Settings
- Base Settings File
```
    app/app/settings/base.py
```
- Development Settings File
```
    app/app/settings/dev.pyName Stmts Miss Cover Missing
```
- Production Settings File
```
    app/app/settings/prod.py
```

## Deployment
- Update settings in app/app/settings/prod.py
- Update DJANGO_SETTINGS_MODULE env var to use ``` app.settings.prod ```
- Update other environment variables listed in the ``` .env ``` file
