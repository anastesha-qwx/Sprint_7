import requests
from api.urls import BaseURL
from api.endpoints import Endpoints


class OrderAPI:

    @staticmethod
    def create(data):
        return requests.post(BaseURL.BASE + Endpoints.ORDER_CREATE, json=data)

    @staticmethod
    def list_orders():
        return requests.get(BaseURL.BASE + Endpoints.ORDERS_LIST)

    @staticmethod
    def get_by_track(track):
        return requests.get(BaseURL.BASE + Endpoints.ORDER_TRACK, params={"t": track})

    @staticmethod
    def accept(order_id, courier_id=None):
        return requests.put(
            BaseURL.BASE + Endpoints.ORDER_ACCEPT + str(order_id),
            params={"courierId": courier_id}
        )
