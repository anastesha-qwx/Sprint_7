import allure
from clients.order_api import OrderAPI
from data.order_data import OrderData


class TestGetOrderByTrack:

    @allure.title("Получение заказа по треку — 200 + order")
    def test_get_order_success(self):
        track = OrderAPI.create(OrderData.base()).json()["track"]
        response = OrderAPI.get_by_track(track)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body

    @allure.title("Нет параметра track — 400")
    def test_get_order_without_track(self):
        response = OrderAPI.get_by_track(track=None)
        assert response.status_code == 400

    @allure.title("Неизвестный track — 404 + понятное сообщение")
    def test_get_order_unknown_track(self):
        response = OrderAPI.get_by_track(9_999_999)
        body = response.json()

        assert response.status_code == 404
        msg = (body.get("message") or "").lower()
        assert ("заказ" in msg) and ("не найден" in msg or "не существует" in msg)
