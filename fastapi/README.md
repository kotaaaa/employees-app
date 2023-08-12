[![Black - Python Formatter](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# Run

```Shell
# build without no-cache
$ docker-compose build --no-cache
$ docker-compose up
$ docker-compose down
```

# Sample Data insert

```Shell
$ docker-compose exec employees-app poetry run python -m api.migrate_db
```

# Go to mysql CLI

```Shell
$ docker-compose exec db mysql employees
# to set encoding utf8
mysql> CHARSET utf8;
```

# Test

```Shell
$ docker-compose run --entrypoint "poetry run pytest --asyncio-mode=auto" employees-app
```

# Swagger UI

```Shell
http://localhost:8000/docs
```
