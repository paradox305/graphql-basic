# Update to a base image of python
FROM python:3.10-slim-buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libpq-dev

# Install poetry
ENV POETRY_HOME=/opt/poetry
RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==1.2.0
RUN $POETRY_HOME/bin/poetry --version

# Install Project Dependencies
COPY ./pyproject.toml ./poetry.lock* /app/
WORKDIR /app
RUN $POETRY_HOME/bin/poetry config virtualenvs.create false \
    && $POETRY_HOME/bin/poetry install --no-dev --no-interaction 

# Copy Project
COPY . /app

# Install pip dependencies
RUN ["pip","install", "graphene<3" ,"flask-graphql==2.0.1"]

# Expose port
EXPOSE 5000

# Start the app
ENTRYPOINT ["python3", "app.py"]