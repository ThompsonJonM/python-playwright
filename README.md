# Python Playwright Project

A testing repository using Python 3.9, Pytest, and Playwright.

1. [Tools Used](#tools-used)
2. [Installation](#installation)
3. [Running Tests](#running-tests)

### Tools Used
- Python 3.9
- Pytest
- Pytest-Asyncio
- Pytest-Playwright
- Playwright
- Flake8
- Black
- Isort
- Pydocstyle
- Pipenv

### Installation
Converted to Pipenv to remove the dependency on virtualenv and pip. Simply install pipenv (`pip install pipenv`), then run `pipenv --python 3.9`. This will build a new virtual environment. Run `pipenv run shell` to activate the environment. Finally, run `pipenv install` to install all dependencies.

It is likely that I will switch this over to Poetry as I have had great experience with the package. In addition, it uses `pyproject.toml` instead of `Pipfile` or `requirements.txt` for dependency management. 

### Running Tests
Run the following commands:

- `pytest` - To run all tests
- `pytest -m {mark}` To run all tests for a certain mark (located in the pyproject.toml file)
- `pytest --headful` To run all tests in a headful state
- `pytest --browser {browser_choice}` To run all tests in a specific browser (chromium, webkit, or firefox)

Each command can be combined such as `pytest -m elements --headful --browser chromium`
