import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


@allure.title("Создание курьера")
class TestCreateCourier:

    def test_create_courier_success(self, courier_payload):
        with allure.step("Отправляем запрос создания курьера"):
            response = CourierAPI.create(courier_payload)
        assert response.status_code == 201
        assert response.json().get("ok") is True

    def test_create_same_courier_twice(self, courier_payload):
        CourierAPI.create(courier_payload)
        response = CourierAPI.create(courier_payload)
        assert response.status_code == 409

    def test_no_login_field(self):
        response = CourierAPI.create(CourierData.no_login())
        assert response.status_code == 400

    def test_no_password_field(self):
        response = CourierAPI.create(CourierData.no_password())
        assert response.status_code == 400
