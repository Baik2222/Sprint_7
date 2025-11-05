import allure
import pytest

from api.courier import CourierAPI
from data.courier import CourierTestData
from data.expected import CourierExpected


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание нового курьера")
    def test_can_create_courier(self, new_courier):
        courier = CourierAPI()

        response = courier.register(new_courier)

        result = response.json()

        assert response.status_code == 201, f"Ожидается 201, получен {response.status_code}"
        assert result.get("ok") is True

    @allure.title("Попытка создать курьера с уже существующим логином")
    def test_cannot_create_duplicate_courier(self, new_courier):
        courier = CourierAPI()

        courier.register(new_courier)
        response = courier.register(new_courier)

        result = response.json()

        assert response.status_code == 409, f"Ожидается 409, получен {response.status_code}"
        assert result.get("message") == CourierExpected.DUPLICATE_LOGIN, result.get("message")

    @allure.title("Отсутствие обязательных полей при создании курьера")
    @pytest.mark.parametrize("data", CourierTestData.MISSING_FIELDS)
    def test_create_courier_missing_fields(self, data):
        courier = CourierAPI()

        response = courier.register(data)
        result = response.json()

        assert response.status_code == 400, f"Ожидается 400, получен {response.status_code}"
        assert result.get("message") == CourierExpected.REGISTER_MISSING_FIELDS
