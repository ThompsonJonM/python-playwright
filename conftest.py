from typing import Union

import pytest
from pytest import fixture

from utilities.api_helpers.api import API

api = API()
domain: str = "www.demoqa.com"
path: str = "/"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: fixture) -> dict:
    response: Union[dict, str] = api.authenticate()
        
    return {
        **browser_context_args,
        "storage_state": {
            "cookies": [
                {
                    "name": "token",
                    "value": response["token"],
                    "path": path,
                    "domain": domain,
                },
                {
                    "name": "userName",
                    "value": response["username"],
                    "path": path,
                    "domain": domain,
                },
                {
                    "name": "userID",
                    "value": response["userId"],
                    "path": path,
                    "domain": domain,
                },
                {
                    "name": "expires",
                    "value": response["expires"],
                    "path": path,
                    "domain": domain,
                },
            ]
        },
    }
