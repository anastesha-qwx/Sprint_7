import allure
from clients.order_api import OrderAPI
from clients.courier_api import CourierAPI
from data.courier_data import CourierData
from data.order_data import OrderData


class TestAcceptOrder:

    @allure.title("Курьер может успешно принять заказ — 200 + ok=true")
    def test_accept_order_success(self):
        courier = CourierData.valid()
        CourierAPI.create(courier)
        courier_id = CourierAPI.login(courier).json()["id"]

        order = OrderData.base()
        track = OrderAPI.create(order).json()["track"]
        order_id = OrderAPI.get_by_track(track).json()["order"]["id"]

        response = OrderAPI.accept(order_id, courier_id)
        body = response.json()

        assert response.status_code == 200
        assert body.get("ok") is True

    @allure.title("Нельзя принять заказ без courierId — 400 + понятное сообщение")
    def test_accept_without_courier_id(self):
        response = OrderAPI.accept(order_id=123, courier_id=None)
        body = response.json()

        assert response.status_code == 400
        msg = (body.get("message") or "").lower()
        assert "недостаточно данных" in msg or "не указан" in msg

    @allure.title("Нельзя принять заказ с несуществующим courierId — 404 + понятное сообщение")
    def test_accept_with_unknown_courier(self):
        response = OrderAPI.accept(order_id=123, courier_id=999_999)
        body = response.json()

        assert response.status_code == 404
        msg = (body.get("message") or "").lower()
        assert ("курьер" in msg) and ("не найден" in msg or "не существует" in msg)

    @allure.title("Нельзя принять несуществующий заказ — 404 + понятное сообщение")
    def test_accept_unknown_order(self):
        courier = CourierData.valid()
        CourierAPI.create(courier)
        courier_id = CourierAPI.login(courier).json()["id"]

        response = OrderAPI.accept(order_id=999_999, courier_id=courier_id)
        body = response.json()

        assert response.status_code == 404
        msg = (body.get("message") or "").lower()
        # покрываем «заказ/заказа» и «не найден/не существует»
        assert ("заказ" in msg) and ("не найден" in msg or "не существует" in msg)
