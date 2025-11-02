from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CourierTestData:
    MISSING_FIELDS: list[dict[str, Any]] = (
        (
            {"login": "", "password": "str123", "firstName": "Vasya"},
            {"login": "user123", "password": "", "firstName": "Vasya"},
            {"login": "", "password": "", "firstName": ""},
        )
    )

    MISSING_LOGIN_FIELDS: list[dict[str, Any]] = (
        (
            {"login": "", "password": "str123"},
            {"login": "user789", "password": ""},
        )
    )
