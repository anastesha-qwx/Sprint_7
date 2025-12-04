import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


@allure.title("Логин курьера")
class TestLoginCourier:

    def test_login_success(self, registered_courier):
        payload = registered_courier["payload"]
        response = CourierAPI.login(payload)
        assert response.status_code == 200
        assert "id" in response.json()

    def test_no_login(self):
        response = CourierAPI.login(CourierData.no_login())
        assert response.status_code == 400

    def test_no_password(self):
        response = CourierAPI.login(CourierData.no_password())
        assert response.status_code == 400

    def test_unknown_user(self):
        response = CourierAPI.login(CourierData.unknown())
        assert response.status_code == 404
