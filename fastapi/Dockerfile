# Download image of python3.9
FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /src
# copy current contents to /src
COPY . .
# Install poetry using pip
RUN pip install poetry
RUN poetry install --no-root
# run uvicorn server
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0"]

