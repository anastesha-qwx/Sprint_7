from api.urls import BaseURL


class Endpoints:
    # Курьеры
    COURIER_CREATE = "/api/v1/courier"
    COURIER_LOGIN = "/api/v1/courier/login"
    COURIER_DELETE = "/api/v1/courier/"

    # Заказы
    ORDER_CREATE = "/api/v1/orders"
    ORDERS_LIST = "/api/v1/orders"
    ORDER_TRACK = "/api/v1/orders/track"
    ORDER_ACCEPT = "/api/v1/orders/accept/"

    @staticmethod
    def make_url(path: str) -> str:
        """Полный URL к пути API, склеенный с базовым адресом стенда."""
        return f"{BaseURL.BASE}{path}"
