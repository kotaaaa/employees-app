# Download image of python3.9
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src
# copy current contents to /src
COPY . .
# Install poetry using pip
RUN pip install poetry

# Copy the definition file of poetry (if it exists)
COPY pyproject.toml* poetry.lock* ./

# Install the library with poetry (if pyproject.toml already exists)
RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install; fi

# Insert initial data to db
RUN poetry run python -m api.migrate_db
# run uvicorn server
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0"]
