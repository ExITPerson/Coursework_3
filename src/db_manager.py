import psycopg2


class DBManager:

    def __init__(self, params, database_name):
        self.database_name = database_name
        self.__params = params
        self.__conn = psycopg2.connect(dbname=self.database_name, **self.__params)
        self.__cur = self.__conn.cursor()


    def get_companies_and_vacancies_count(self):
        self.__cur.execute(
            """
            SELECT employee_id, company_name, count_open_vacancies FROM employees
            """
        )
        result = self.__cur.fetchall()
        return result


    def get_all_vacancies(self):
        self.__cur.execute(
            """
            SELECT company_name, vacancy_name, salary, vacancy_url FROM vacancies
            JOIN employees USING(employee_id)
            """
        )
        result = self.__cur.fetchall()
        return result


    def get_avg_salary(self):
        self.__cur.execute(
            """
            SELECT to_char(ROUND(AVG(salary), 2), 'FM999999990.00') FROM vacancies
            WHERE salary IS NOT NULL
            """
        )
        result = self.__cur.fetchall()
        return result[0]

    def get_vacancies_with_higher_salary(self):
        self.__cur.execute(
            """
            SELECT * FROM vacancies
            WHERE salary > (SELECT AVG(salary) FROM vacancies)
            """
        )
        result = self.__cur.fetchall()
        return result


    def vacancies_with_keyword(self, key):
        self.__cur.execute(
            f"""
            SELECT * FROM vacancies
            WHERE vacancy_name LIKE '%{key}%'
            """
        )
        result = self.__cur.fetchall()
        return result


    def close(self):
        self.__cur.close()
        self.__conn.close()