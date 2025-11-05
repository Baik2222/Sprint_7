import pytest

from api.courier import CourierAPI
from api.order import OrderAPI
from core.utils import generate_random_string, register_new_courier
from data.order import OrderTestData


@pytest.fixture()
def courier_credentials():
    courier = CourierAPI()
    db = register_new_courier()

    login, password, *_ = db
    data = {"login": login, "password": password}

    yield db

    result = courier.login(data)
    courier_id = result.json().get("id") if result.status_code == 200 else None
    if courier_id:
        courier.delete(courier_id)


@pytest.fixture
def new_courier():
    courier = CourierAPI()

    data = {
        "login": generate_random_string(12),
        "password": generate_random_string(12),
        "firstName": generate_random_string(12)
    }

    yield data

    result = courier.login({"login": data["login"], "password": data["password"]})
    courier_id = result.json().get("id") if result.status_code == 200 else None
    if courier_id:
        courier.delete(courier_id)


@pytest.fixture
def created_order():
    order = OrderAPI()

    response = order.create(OrderTestData.COLORS[0])
    track = response.json().get("track")

    yield track

    if track:
        order.cancel(track)
