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

### Installation
Prior to install, you should create a virtual environment using Python 3.9. Once created, source the virtual environment. Following activation, run the following in the directory root: `pip install requirements.txt`. This should install all requirements found in the text file.

To verify install, run `pytest --version`. It should read `6.2.2` per the requirements.

### Running Tests
Run the following commands:

`pytest` - To run all tests
`pytest -m {mark}` To run all tests for a certain mark (located in the pyproject.toml file)
`pytest --headful` To run all tests in a headful state
`pytest --browser {browser_choice}` To run all tests in a specific browser (chromium, webkit, or firefox)

Each command can be combined such as `pytest -m elements --headful --browser chromium`
