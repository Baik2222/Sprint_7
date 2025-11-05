import allure
import requests
from requests import Response

from constants.endpoints import OrderRoute


class OrderAPI:

    @allure.step("Создание заказа")
    def create(self, data: dict) -> Response:
        return requests.post(OrderRoute.CREATE, json=data)

    @allure.step("Получение списка заказов")
    def list(self) -> Response:
        return requests.get(OrderRoute.LIST)

    @allure.step("Отмена заказа")
    def cancel(self, track_num: int) -> Response:
        return requests.put(f"{OrderRoute.CANCEL}/{track_num}")
