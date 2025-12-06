import requests
import allure
from api.endpoints import Endpoints


class CourierAPI:
   

    @staticmethod
    @allure.step("Создаём курьера")
    def create(data: dict):
        """POST /api/v1/courier — JSON"""
        url = Endpoints.make_url(Endpoints.COURIER_CREATE)
        return requests.post(url, json=data)

    @staticmethod
    @allure.step("Логиним курьера")
    def login(data: dict):
        """POST /api/v1/courier/login — form-data!"""
        url = Endpoints.make_url(Endpoints.COURIER_LOGIN)
        return requests.post(url, data=data)  

    @staticmethod
    @allure.step("Удаляем курьера по id = {courier_id}")
    def delete(courier_id: int):
        """DELETE /api/v1/courier/{id}"""
        url = Endpoints.make_url(Endpoints.COURIER_DELETE) + str(courier_id)
        return requests.delete(url)

