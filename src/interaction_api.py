import requests
import json


def get_list_employers(employer_ids):
    """Получение данных о работадателях"""
    result = []
    for employer_id in employer_ids:
        url = f"https://api.hh.ru/employers/{employer_id}"
        headers = {"User-Agent": "HH-User-Agent"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result.append(response.json())
        else:
            raise BaseException(f"Код ошибки: {response.status_code}")
    return result

def get_vacancies(employers):
    """Получение данных о вакансиях работадателей"""
    for employer in employers:
        vacancies = employer["vacancies_url"]
        headers = {"User-Agent": "HH-User-Agent"}
        response = requests.get(vacancies, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise BaseException(f"Код ошибки: {response.status_code}")
