import requests

from src.abs_classes import AbstractAPIJob


class HeadHunterAPI(AbstractAPIJob):
    """Класс для получения информации о работадателях и вакансиях из сервиса HH"""

    def __init__(self, employers_ids: list) -> None:
        self.__url: str = "https://api.hh.ru/employers/"
        self.__headers: dict = {"User-Agent": "HH-User-Agent"}
        self.__data: list = []
        self.employers_ids: list[str] = employers_ids

    def __connection_api(self, url):
        """Подключение к API и получение данных"""

        response = requests.get(url, headers=self.__headers)

        if response.status_code == 200:
            return response.json()

        else:
            raise BaseException(f"Статус код: {response.status_code}")

    def get_info(self) -> list[dict]:
        """Преобразование данных для дальнейшего использования"""

        data = []

        for emp_id in self.employers_ids:

            emp = self.__connection_api(str(self.__url + emp_id))

            vacancies = self.__connection_api(emp["vacancies_url"])

            data.append({"employer": emp, "vacancies": vacancies["items"]})

        return data
