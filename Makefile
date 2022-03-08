DOCKER := docker
FILE_NAME := open_chrome.py

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

# Executing only in terminal

.PHONY: run
run: build
	python3 open_chrome.py
