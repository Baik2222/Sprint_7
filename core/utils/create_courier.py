import requests

from constants.endpoints import CourierRoute
from .string_tools import generate_random_string


def register_new_courier() -> list[str]:
    login_pass = []

    login = generate_random_string(12)
    password = generate_random_string(12)
    first_name = generate_random_string(12)

    data = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(CourierRoute.CREATE, data=data)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass
