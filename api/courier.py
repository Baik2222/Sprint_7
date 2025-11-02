import requests
from requests import Response

from constants.endpoints import CourierRoute


class CourierAPI:

    def register(self, data: dict) -> Response:
        return requests.post(CourierRoute.CREATE, json=data)

    def login(self, data: dict) -> Response:
        return requests.post(CourierRoute.LOGIN, json=data)

    def delete(self, courier_id: int) -> Response:
        return requests.delete(f"{CourierRoute.DELETE}/{courier_id}")
