__all__ = ["BASE_URL", "CourierRoute", "OrderRoute"]

BASE_URL = "https://qa-scooter.praktikum-services.ru"
API_V1 = f"{BASE_URL}/api/v1"


class CourierRoute:
    CREATE = f"{API_V1}/courier"
    LOGIN = f"{API_V1}/courier/login"
    DELETE = f"{API_V1}/courier"


class OrderRoute:
    CREATE = f"{API_V1}/orders"
    LIST = f"{API_V1}/orders"
    CANCEL = f"{API_V1}/orders/cancel"
