import pytest
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


@pytest.fixture
def courier_payload():
    return CourierData.valid()


@pytest.fixture
def registered_courier(courier_payload):
    CourierAPI.create(courier_payload)
    login_response = CourierAPI.login(courier_payload)
    courier_id = login_response.json().get("id")
    return {"id": courier_id, "payload": courier_payload}


@pytest.fixture
def new_order():
    from clients.order_api import OrderAPI
    from data.order_data import OrderData

    payload = OrderData.base()
    response = OrderAPI.create(payload)
    track = response.json()["track"]
    return {"track": track}
