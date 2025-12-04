import allure
from clients.order_api import OrderAPI
from data.order_data import OrderData


@allure.title("Получение заказа по треку")
class TestGetOrderByTrack:

    def test_get_order_success(self):
        track = OrderAPI.create(OrderData.base()).json()["track"]
        response = OrderAPI.get_by_track(track)
        assert response.status_code == 200
        assert "order" in response.json()

    def test_get_order_without_track(self):
        response = OrderAPI.get_by_track("")
        assert response.status_code == 400

    def test_get_order_unknown_track(self):
        response = OrderAPI.get_by_track(9999999)
        assert response.status_code == 404
