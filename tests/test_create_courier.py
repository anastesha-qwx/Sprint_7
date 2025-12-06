import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


class TestCreateCourier:

    @allure.title("Успешное создание курьера — 201 + ok=true")
    def test_create_courier_success(self, courier_payload):
        with allure.step("Отправляем запрос создания курьера"):
            response = CourierAPI.create(courier_payload)
        body = response.json()

        assert response.status_code == 201
        assert body.get("ok") is True

    @allure.title("Нельзя создать двух одинаковых курьеров — 409 + сообщение о занятости логина")
    def test_create_same_courier_twice(self, courier_payload):
        CourierAPI.create(courier_payload)
        response = CourierAPI.create(courier_payload)
        body = response.json()

        assert response.status_code == 409
        assert "логин" in (body.get("message") or "").lower()

    @allure.title("Нет поля login — 400 + сообщение о недостаточных данных")
    def test_no_login_field(self):
        response = CourierAPI.create(CourierData.no_login())
        body = response.json()

        assert response.status_code == 400
        msg = (body.get("message") or "").lower()
        assert "недостаточно данных" in msg

    @allure.title("Нет поля password — 400 + сообщение о недостаточных данных")
    def test_no_password_field(self):
        response = CourierAPI.create(CourierData.no_password())
        body = response.json()

        assert response.status_code == 400
        msg = (body.get("message") or "").lower()
        assert "недостаточно данных" in msg
