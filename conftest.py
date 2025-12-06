import pytest
import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


@pytest.fixture
def courier_payload():
    return CourierData.valid()


@pytest.fixture
def registered_courier(courier_payload):
    """Создаёт курьера, логинит и по завершению теста удаляет его."""
    with allure.step("Создаём курьера для теста"):
        CourierAPI.create(courier_payload)
    with allure.step("Логиним курьера и получаем id"):
        login_response = CourierAPI.login(courier_payload)
        courier_id = login_response.json().get("id")

    yield {"id": courier_id, "payload": courier_payload}

    # teardown
    if courier_id:
        with allure.step(f"Удаляем тестового курьера id={courier_id}"):
            CourierAPI.delete(courier_id)


@pytest.fixture
def new_order():
    """Создаёт заказ и возвращает track."""
    from clients.order_api import OrderAPI
    from data.order_data import OrderData

    payload = OrderData.base()
    response = OrderAPI.create(payload)
    track = response.json().get("track")
    return {"track": track}

