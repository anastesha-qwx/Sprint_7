import allure
from clients.order_api import OrderAPI


class TestOrdersList:

    @allure.title("Получение списка заказов — 200 + orders[]")
    def test_get_orders(self):
        response = OrderAPI.list_orders()
        body = response.json()

        assert response.status_code == 200
        assert "orders" in body
        assert isinstance(body["orders"], list)
