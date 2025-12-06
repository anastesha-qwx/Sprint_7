from faker import Faker

fake = Faker("ru_RU")


class CourierData:

    @staticmethod
    def valid():
        return {
            "login": fake.user_name(),
            "password": fake.password(),
            "firstName": fake.first_name()
        }

    @staticmethod
    def no_login():
        data = CourierData.valid()
        data["login"] = ""
        return data

    @staticmethod
    def no_password():
        data = CourierData.valid()
        data["password"] = ""
        return data

    @staticmethod
    def unknown():
        return {"login": "non_exist_user", "password": "123456"}
