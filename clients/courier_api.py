import requests
from api.urls import BaseURL
from api.endpoints import Endpoints


class CourierAPI:

    @staticmethod
    def create(data):
        return requests.post(BaseURL.BASE + Endpoints.COURIER_CREATE, data=data)

    @staticmethod
    def login(data):
        return requests.post(BaseURL.BASE + Endpoints.COURIER_LOGIN, data=data)

    @staticmethod
    def delete(courier_id):
        return requests.delete(BaseURL.BASE + Endpoints.COURIER_DELETE + str(courier_id))
