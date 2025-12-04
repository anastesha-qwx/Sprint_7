import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


@allure.title("Удаление курьера")
class TestDeleteCourier:

    def test_delete_courier_success(self):
        data = CourierData.valid()
        CourierAPI.create(data)
        courier_id = CourierAPI.login(data).json()["id"]

        response = CourierAPI.delete(courier_id)
        assert response.status_code == 200
        assert response.json().get("ok") is True

    def test_delete_without_id(self):
        response = CourierAPI.delete("")
        assert response.status_code == 404

    def test_delete_unknown_id(self):
        response = CourierAPI.delete(9999999)
        assert response.status_code == 404
