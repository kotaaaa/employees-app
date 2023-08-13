[![Black - Python Formatter](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# Employees Management App

![](demo.png)

### Functional Requirements:

- Initially, list all employees that are in data.json
  - First name, last name, and salary in currency format (ie. $42,000)
- The ability to edit an employee
- The ability to delete an employee
- The ability to create a new employee

# prerequisite

- Docker
- docker-compose

```
# For Your Information
$ docker-compose version
Docker Compose version v2.15.1
```

# 1, Run with docker-compose

```Shell
# You can run whole app with just one command
$ docker-compose build --no-cache && docker-compose up
```

# 2, Sample Data insert Manually

```Shell
$ docker-compose exec employees-app poetry run python -m api.migrate_db
```

Then, you can check how the application works.
Go to http://localhost:8080/

# Another useful command

## Go to mysql CLI

```Shell
$ docker-compose exec db mysql employees
# to set encoding utf8
mysql> CHARSET utf8;
mysql> desc employees;
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| id         | int           | NO   | PRI | NULL    | auto_increment |
| first_name | varchar(1024) | YES  |     | NULL    |                |
| last_name  | varchar(1024) | YES  |     | NULL    |                |
| salary     | int           | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+
4 rows in set (0.02 sec)
```

## Run Unit Test (FastAPI)

```Shell
$ docker-compose run --entrypoint "poetry run pytest --asyncio-mode=auto" employees-app
```

## Swagger UI (You can check API Specification here)

```Shell
http://localhost:8000/docs
```

## Run Frontend(Vue.js) mannually

Node version: 16.5.0

```
$ cd front-app
$ yarn install
$ yarn serve
```
