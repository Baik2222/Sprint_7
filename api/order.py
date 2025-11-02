import requests
from requests import Response

from constants.endpoints import OrderRoute


class OrderAPI:

    def create(self, data: dict) -> Response:
        return requests.post(OrderRoute.CREATE, json=data)

    def list(self) -> Response:
        return requests.get(OrderRoute.LIST)

    def cancel(self, track_num: int) -> Response:
        return requests.put(f"{OrderRoute.CANCEL}/{track_num}")
