PY ?= python3
.PHONY: install test install-ci test-ci

install:
	$(PY) -m pip install -U pip
	$(PY) -m pip install .

install-ci:
	$(PY) -m pip install -U pip
	$(PY) -m pip install -r requirements-dev.txt
	$(PY) -m pip install .

test:
	pre-commit run --all-files
	$(PY) -m pytest tests/

test-ci:
	$(PY) -m pytest -vv tests/ --cov cptk/ --cov-report xml --cov-report term
