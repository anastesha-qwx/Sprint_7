import requests
import allure
from api.endpoints import Endpoints


class OrderAPI:

    @staticmethod
    @allure.step("Создаём заказ")
    def create(data: dict):
        url = Endpoints.make_url(Endpoints.ORDER_CREATE)
        return requests.post(url, json=data)

    @staticmethod
    @allure.step("Получаем заказ по треку = {track}")
    def get_by_track(track: int | None):
        url = Endpoints.make_url(Endpoints.ORDER_TRACK)
        params = None if track is None else {"t": track}
        return requests.get(url, params=params)

    @staticmethod
    @allure.step("Получаем список заказов")
    def list_orders():
        url = Endpoints.make_url(Endpoints.ORDERS_LIST)
        return requests.get(url)

    @staticmethod
    @allure.step("Курьер {courier_id} принимает заказ {order_id}")
    def accept(order_id: int, courier_id: int | None):
        url = Endpoints.make_url(Endpoints.ORDER_ACCEPT) + str(order_id)
        return requests.put(url, params={"courierId": courier_id})
