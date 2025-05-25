import requests


def get_list_employers(employer_id):
    url = f"https://api.hh.ru/employers/{employer_id}"
    headers = {"User-Agent": "HH-User-Agent"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise BaseException(f"Код ошибки: {response.status_code}")

def get_vacancies(employers):
    for employer in employers:
        vacancies = employer["vacancies_url"]
        headers = {"User-Agent": "HH-User-Agent"}
        response = requests.get(vacancies, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BaseException(f"Код ошибки: {response.status_code}")
