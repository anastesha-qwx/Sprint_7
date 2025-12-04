import allure
import pytest
from clients.order_api import OrderAPI
from data.order_data import OrderData


@allure.title("Создание заказа")
class TestOrderCreate:

    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_order_colors(self, colors):
        payload = OrderData.base()
        payload["color"] = colors

        response = OrderAPI.create(payload)
        assert response.status_code == 201
        assert "track" in response.json()
