import allure
import requests
from requests import Response

from constants.endpoints import CourierRoute


class CourierAPI:

    @allure.step("Регистрация курьера")
    def register(self, data: dict) -> Response:
        return requests.post(CourierRoute.CREATE, json=data)

    @allure.step("Авторизация курьера")
    def login(self, data: dict) -> Response:
        return requests.post(CourierRoute.LOGIN, json=data)

    @allure.step("Удаление курьера")
    def delete(self, courier_id: int) -> Response:
        return requests.delete(f"{CourierRoute.DELETE}/{courier_id}")
