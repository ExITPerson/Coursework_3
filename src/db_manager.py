from typing import Any

import psycopg2

from src.abs_classes import AbsDBManager


class DBManager(AbsDBManager):
    """ Класс для взаимодействия с БД и получения данных"""

    def __init__(self, params: dict, database_name: str) -> None:
        self.database_name: str = database_name
        self.__params: dict = params
        self.__conn = psycopg2.connect(dbname=self.database_name, **self.__params)
        self.__cur = self.__conn.cursor()

    def get_companies_and_vacancies_count(self) -> Any:
        """Функция для получения из БД списка компаний и кол-во вакансий у них"""

        self.__cur.execute(
            """
            SELECT employee_id, company_name, count_open_vacancies FROM employees
            """
        )
        result = self.__cur.fetchall()
        return result

    def get_all_vacancies(self) -> Any:
        """Функция для получения из БД списка вакансий"""

        self.__cur.execute(
            """
            SELECT company_name, vacancy_name, salary, vacancy_url FROM vacancies
            JOIN employees USING(employee_id)
            """
        )
        result = self.__cur.fetchall()
        return result

    def get_avg_salary(self) -> Any:
        """Функция для получения из БД средней зарплаты по всем вакансиям"""

        self.__cur.execute(
            """
            SELECT to_char(ROUND(AVG(salary), 2), 'FM999999990.00') FROM vacancies
            WHERE salary IS NOT NULL
            """
        )
        result = self.__cur.fetchall()
        return result[0]

    def get_vacancies_with_higher_salary(self) -> Any:
        """Функция для получения из БД списка вакансий с зарплатами выше среднего"""

        self.__cur.execute(
            """
            SELECT * FROM vacancies
            WHERE salary > (SELECT AVG(salary) FROM vacancies)
            """
        )
        result = self.__cur.fetchall()
        return result

    def get_vacancies_with_keyword(self, key: str) -> Any:
        """Функция для получения из БД списка вакансий по ключевому слову в названиях"""

        self.__cur.execute(
            f"""
            SELECT * FROM vacancies
            WHERE vacancy_name LIKE '%{key}%'
            """
        )
        result = self.__cur.fetchall()
        return result

    def close(self) -> None:
        """Функция для отключения от БД"""

        self.__cur.close()
        self.__conn.close()
