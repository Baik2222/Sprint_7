import allure
import pytest

from api.courier import CourierAPI
from core.utils import generate_random_string
from data.courier import CourierTestData


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Создание нового курьера")
    def test_can_create_courier(self):
        courier = CourierAPI()

        data = {
            "login": generate_random_string(12),
            "password": generate_random_string(12),
            "firstName": generate_random_string(12)
        }

        response = courier.register(data)
        result = response.json()

        assert response.status_code == 201, f"Ожидается 201, получен {response.status_code}"
        assert result.get("ok") == True

        courier_id = courier.login(data).json().get("id")
        courier.delete(courier_id)

    @allure.title("Попытка создать курьера с уже существующим логином")
    def test_cannot_create_duplicate_courier(self):
        courier = CourierAPI()

        data = {
            "login": generate_random_string(12),
            "password": generate_random_string(12),
            "firstName": generate_random_string(12)
        }

        courier.register(data)
        response = courier.register(data)

        result = response.json()

        assert response.status_code == 409, f"Ожидается 409, получен {response.status_code}"
        assert result.get("message") == "Этот логин уже используется. Попробуйте другой.", result.get("message")

        courier_id = courier.login(data).json().get("id")
        courier.delete(courier_id)

    @allure.title("Отсутствие обязательных полей при создании курьера")
    @pytest.mark.parametrize("data", CourierTestData.MISSING_FIELDS)
    def test_create_courier_missing_fields(self, data):
        courier = CourierAPI()

        response = courier.register(data)
        result = response.json()

        assert response.status_code == 400, f"Ожидается 400, получен {response.status_code}"
        assert result.get("message") == "Недостаточно данных для создания учетной записи"
