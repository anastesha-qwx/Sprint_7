import allure
from clients.order_api import OrderAPI
from clients.courier_api import CourierAPI
from data.courier_data import CourierData
from data.order_data import OrderData


@allure.title("Принятие заказа курьером")
class TestAcceptOrder:

    def test_accept_order_success(self):
        courier = CourierData.valid()
        CourierAPI.create(courier)
        courier_id = CourierAPI.login(courier).json()["id"]

        order = OrderData.base()
        track = OrderAPI.create(order).json()["track"]
        order_id = OrderAPI.get_by_track(track).json()["order"]["id"]

        response = OrderAPI.accept(order_id, courier_id)
        assert response.status_code == 200
        assert response.json()["ok"] is True

    def test_accept_without_courier_id(self):
        response = OrderAPI.accept(order_id=123, courier_id=None)
        assert response.status_code == 400

    def test_accept_with_unknown_courier(self):
        response = OrderAPI.accept(order_id=123, courier_id=999999)
        assert response.status_code in [400, 404]

    def test_accept_unknown_order(self):
        courier = CourierData.valid()
        CourierAPI.create(courier)
        courier_id = CourierAPI.login(courier).json()["id"]

        response = OrderAPI.accept(order_id=999999, courier_id=courier_id)
        assert response.status_code in [400, 404]
