# Makefile tutorial-sqlalchemy

# These targets are not files
.PHONY: all help clean clean-build clean-others clean-pyc clean-test run validate requirements test testx test-collect coverage coverage-html pep8 check.test_path

check.test_path:
	@if test "$(TEST_PATH)" = "" ; then echo "TEST_PATH is undefined. The default is tests."; fi

all: help

help:
	@echo 'Makefile *** tutorial-sqlalchemy *** Makefile'

clean: clean-build clean-others clean-pyc clean-test run validate requirements test coverage coverage.html pep8

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-others:
	@find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	@rm -fr .tox/
	@rm -f .coverage
	@rm -fr htmlcov/

requirements:
	@pip install -r requirements.txt

test: check.test_path
	@py.test -s $(TEST_PATH) --basetemp=tests/media --disable-pytest-warnings

testx: check.test_path
	@py.test -s -x $(TEST_PATH) --basetemp=tests/media --disable-pytest-warnings

test-collect: check.test_path
	@py.test -s $(TEST_PATH) --basetemp=tests/media --collect-only --disable-pytest-warnings

coverage: check.test_path
	@py.test -s $(TEST_PATH) --cov --basetemp=tests/media --disable-pytest-warnings

coverage-html: check.test_path
	@py.test -s $(TEST_PATH) --cov --cov-report=html --basetemp=tests/media --disable-pytest-warnings

pep8:
	@pep8 --filename="*.py" --ignore=W --first --show-source --statistics --count .
