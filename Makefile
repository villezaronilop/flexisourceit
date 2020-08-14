.DEFAULT_GOAL := help

# Local host and port
ADDR = 0.0.0.0
PORT = 8000

APP_PATH = ${app_path}
DB_HOST = $(host)
DB_USER = $(user)
DB_NAME = $(db)
FILE = $(file)

# Given the virtualenv is activated
PYTHON_CMD = python

DJANGO_MANAGE_PATH = manage.py
DJANGO_MANAGE_CMD = ${PYTHON_CMD} ${DJANGO_MANAGE_PATH}

COMMAND = ${COMMAND}

help:
	@echo "COMMANDS: "
	@echo "run - run development server."


check.standard:
	pydocstyle
	flake8

format:
	pre-commit run --all-files

migrate:
	${DJANGO_MANAGE_PATH} migrate

migrations:
	${DJANGO_MANAGE_PATH} makemigrations


run:
	${DJANGO_MANAGE_CMD} runserver "$(ADDR):$(PORT)"

shell:
	${DJANGO_MANAGE_CMD} shell_plus

test:
	pytest
