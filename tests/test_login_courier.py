import allure
import pytest

from api.courier import CourierAPI
from core.utils import generate_random_string
from data.courier import CourierTestData
from data.expected import CourierExpected


@allure.suite("Авторизация курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier_credentials):
        courier = CourierAPI()

        response = courier.login({"login": courier_credentials[0], "password": courier_credentials[1]})

        assert response.status_code == 200, f"Ожидается 200, получен {response.status_code}"
        assert response.json().get("id") is not None, "Отсутствует поле 'id'"

    @allure.title("Отсутствует обязательное поле при авторизации")
    @pytest.mark.parametrize("case", CourierTestData.MISSING_LOGIN_FIELDS)
    def test_login_courier_missing_required_fields(self, case):
        courier = CourierAPI()

        response = courier.login({
            "login": case.get("login"),
            "password": case.get("password"),
        })

        assert response.status_code == 400, f"Ожидается 400, получен {response.status_code}"
        assert response.json().get("message") == CourierExpected.LOGIN_MISSING_FIELDS, response.json()

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_with_nonexistent_user_error(self):
        courier = CourierAPI()

        response = courier.login({"login": generate_random_string(12), "password": generate_random_string(12)})

        assert response.status_code == 404, f"Ожидается 404, получен {response.status_code}"
        assert response.json().get("message") == CourierExpected.NOT_FOUND, response.json()

    @allure.title("Авторизация с неверным логином")
    def test_login_courier_invalid_login_error(self, courier_credentials):
        courier = CourierAPI()

        response = courier.login({"login": generate_random_string(12), "password": courier_credentials[1]})

        assert response.status_code == 404, f"Ожидается 404, получен {response.status_code}"
        assert response.json().get("message") == CourierExpected.NOT_FOUND, response.json()

    @allure.title("Авторизация с неверным паролем")
    def test_login_courier_invalid_password_error(self, courier_credentials):
        courier = CourierAPI()

        response = courier.login({"login": courier_credentials[0], "password": generate_random_string(12)})

        assert response.status_code == 404, f"Ожидается 404, получен {response.status_code}"
        assert response.json().get("message") == CourierExpected.NOT_FOUND, response.json()
