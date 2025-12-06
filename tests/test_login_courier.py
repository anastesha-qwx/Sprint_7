import allure
from clients.courier_api import CourierAPI
from data.courier_data import CourierData


class TestLoginCourier:

    @allure.title("Логин успешный — 200 + id")
    def test_login_success(self, registered_courier):
        payload = registered_courier["payload"]
        response = CourierAPI.login(payload)
        body = response.json()

        assert response.status_code == 200
        assert isinstance(body.get("id"), int)

    @allure.title("Нет login — 400 + сообщение")
    def test_no_login(self):
        response = CourierAPI.login(CourierData.no_login())
        body = response.json()

        assert response.status_code == 400
        msg = (body.get("message") or "").lower()
        assert "недостаточно данных" in msg

    @allure.title("Нет password — 400 + сообщение")
    def test_no_password(self):
        response = CourierAPI.login(CourierData.no_password())
        body = response.json()

        assert response.status_code == 400
        msg = (body.get("message") or "").lower()
        assert "недостаточно данных" in msg

    @allure.title("Неизвестный пользователь — 404 + сообщение")
    def test_unknown_user(self):
        response = CourierAPI.login(CourierData.unknown())
        body = response.json()

        assert response.status_code == 404
        msg = (body.get("message") or "").lower()
        assert "учетная запись" in msg and ("не найд" in msg or "не существ" in msg)
