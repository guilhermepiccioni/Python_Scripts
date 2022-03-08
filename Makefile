DOCKER := docker
FILE_NAME := open_chrome.py
DOCKER_COMPOSE = docker-compose
FILE_DOCKER = docker-compose.yaml

.PHONY: build
build:
	$(DOCKER) build .

.PHONY: black
black:
	black $(FILE_NAME)

.PHONY: mypy
mypy:
	mypy $(FILE_NAME)

.PHONY: flake8
flake8:
	flake8 $(FILE_NAME)

.PHONY: bandit
bandit:
	bandit $(FILE_NAME)

.PHONY: lint
lint: black mypy flake8 bandit

.PHONY: scripts_db
scripts_db:
	$(DOCKER_COMPOSE) -f $(FILE_DOCKER) up -d scripts_db

# Executing only in terminal

.PHONY: run
run: build scripts_db
	python3 open_chrome.py
