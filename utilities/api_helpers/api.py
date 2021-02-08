import json
from random import random
from time import sleep
from typing import Union

import requests
from requests import HTTPError, Response

from credentials import user

base_url: str = "https://www.demoqa.com"


class API(object):
    
    @staticmethod
    def authenticate() -> Union[dict, None]:
        _data: dict = user
        _url = f"{base_url}/Account/v1/Login"
        tries: int = 10

        while True:
            tries =- 1

            sleep(random())
            response: Response = requests.post(
                url=_url, data=_data
            )

            if response.status_code == 200:
                return response.json()
            elif tries == 0:
                raise HTTPError(f"Requests failed with response: {response.json()}")