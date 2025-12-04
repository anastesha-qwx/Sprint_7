import allure
from clients.order_api import OrderAPI


@allure.title("Получение списка заказов")
class TestOrdersList:

    def test_get_orders(self):
        response = OrderAPI.list_orders()
        assert response.status_code == 200
        assert "orders" in response.json()
