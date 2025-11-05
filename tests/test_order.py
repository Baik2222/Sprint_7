import allure
import pytest

from api.order import OrderAPI
from data.order import OrderTestData


@allure.suite("Тесты заказов")
class TestOrder:

    @pytest.mark.parametrize("case", OrderTestData.COLORS)
    @allure.title("Успешное создание заказа")
    def test_create_order_various_colors(self, case):
        order = OrderAPI()

        response = order.create(case)
        assert response.status_code == 201, f"Ожидается 201, получен {response.status_code}"

        track_num = response.json().get("track")
        assert track_num is not None, f"Ожидается поле track в ответе"

    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        order = OrderAPI()

        response = order.list()

        assert response.status_code == 200, f"Ожидается 200, получен {response.status_code}"
        assert response.content, f"Ожидается список заказов, получен {response.json()}"
