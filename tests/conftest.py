import pytest

from api.courier import CourierAPI
from core.utils import register_new_courier


@pytest.fixture()
def courier_credentials():
    courier = CourierAPI()
    db = register_new_courier()

    login, password, *_ = db
    data = {"login": login, "password": password}

    yield db

    result = courier.login(data)
    if result.status_code == 200:
        courier.delete(result)
