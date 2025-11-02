from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class OrderTestData:
    COLORS: list[dict[str, Any]] = (
        (
            {
                "firstName": "Ivan", "lastName": "Ivanov", "address": "Lenina Ave, 7",
                "metroStation": 3, "phone": "+7 901 234-56-78", "rentTime": 3, "deliveryDate": "2025-11-11",
                "comment": "All Colors", "color": ["BLACK", "GREY"],
            },
            {
                "firstName": "Sidor", "lastName": "Sidorov", "address": "Tverskaya Street, 8",
                "metroStation": 5, "phone": "+7 902 345-67-89", "rentTime": 3, "deliveryDate": "2025-11-01",
                "comment": "Only one color", "color": ["BLACK"],
            },
            {
                "firstName": "Maxim", "lastName": "Maximov", "address": "Gagarin Street, 12",
                "metroStation": 2, "phone": "+7 903 456-78-91", "rentTime": 4, "deliveryDate": "2025-11-05",
                "comment": "Only one color", "color": ["GREY"],
            },
            {
                "firstName": "Petr", "lastName": "Petrov", "address": "Pushkin Street, 9",
                "metroStation": 3, "phone": "+7 912 345-67-89", "rentTime": 1, "deliveryDate": "2025-12-12",
                "comment": "No color", "color": [],
            },
        )
    )
