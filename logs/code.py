import base64
import os

import requests


class SomeError(Exception):
    pass


class SomeService:
    BASE_URL = "https://some.service.url"

    def __init__(self, some_api_key: str, some_query_id: int, login: str, password: str):
        self.__api_key = some_api_key
        self.__query_id = some_query_id
        self.__login = login
        self.__password = password

    def some_connection(self):
        url = self.BASE_URL + f"/api/{self.__query_id}"
        session = requests.Session()
        session.headers.update({"Authorization": "Key {}".format(self.__api_key)})

        response = session.post(
            url,
            params={"api_key": self.__api_key},
            json={"login": self.__login, "password": self.__password},
        )

        if response.status_code != 200:
            raise SomeError

        return response.json()

    def get_data(self):
        return self.some_connection()


if __name__ == "__main__":
    service = SomeService(
        some_api_key="123",
        some_query_id=1,
        login="docker_login",
        password=base64.b64decode(os.environ.get("PASSWORD")).decode("utf-8"),
    )
    data = service.get_data()
