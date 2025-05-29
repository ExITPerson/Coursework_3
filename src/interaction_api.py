import requests


def get_list_employers(employer_ids):
    """Получение данных о работадателях"""
    data = []

    for employer_id in employer_ids:
        url = f"https://api.hh.ru/employers/{employer_id}"
        headers = {"User-Agent": "HH-User-Agent"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            employer = response.json()

            url_vacancies = employer["vacancies_url"]
            response_vacancies = requests.get(url_vacancies, headers=headers)

            if response_vacancies.status_code == 200:
                vacancies = response_vacancies.json()["items"]

            else:
                raise BaseException(f"Код ошибки: {response_vacancies.status_code}")

        else:
            raise BaseException(f"Код ошибки: {response.status_code}")

        data.append(
            {
                "employer": employer,
                "vacancies": vacancies
            }
        )
    return data
