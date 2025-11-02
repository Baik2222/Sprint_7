# Тестирование API сервиса Яндекс Самокат

---

## Описание проекта

Автоматизация тестирования API веб-приложения [Yandex Scooter](https://qa-scooter.praktikum-services.ru/)

---

## Как установить

1. Установить зависимости:

```
pip install -r requirements.txt
```

---

## Как запустить

Для запуска всех тестов:

```
pytest -v
```

```
pytest --alluredir=allure_results
```

---

## Результаты allure

```
allure serve allure_results
```
