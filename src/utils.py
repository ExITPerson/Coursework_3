import psycopg2


def create_database(database_name, params):
    """Функция для создания базы данных"""

    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE employers (
                employee_id INTEGER,
                name VARCHAR(50) NOT NULL,
                site_url TEXT,
                company_hh_url TEXT,
                area TEXT,
                count_open_vacancies INTEGER,
                description VARCHAR
            )
        """)

    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE vacancies (
                vacancy_id INTEGER,
                employee_id INTEGER,
                name VARCHAR(100) NOT NULL,
                area TEXT,
                salary INTEGER,
                currency TEXT,
                vacancy_url TEXT,
                responsibility VARCHAR
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data, database_name, params):
    """Сохранение данных в базу данных"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cursor:

        for employer in data:
            employer_data = employer["employer"]
            cursor.execute(
                """
                INSERT INTO employers 
                (employee_id, name, site_url, company_hh_url, area, count_open_vacancies, description)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (employer_data["id"], employer_data["name"], employer_data["site_url"],
                 employer_data["alternate_url"], employer_data["area"]["name"], employer_data["open_vacancies"],
                 employer_data["description"])
            )

            vacancies_data = employer["vacancies"]
            for vacancy in vacancies_data:
                cursor.execute(
                    """
                    INSERT INTO vacancies
                    (vacancy_id, employee_id, name, area, salary, currency, vacancy_url, responsibility)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
                    """,
                    (vacancy["id"], vacancy["employer"]["id"], vacancy["name"],
                     vacancy["area"]["name"], (vacancy["salary"]["from"] if vacancy["salary"] is not None else None),
                     (vacancy["salary"]["currency"] if vacancy["salary"] is not None else None),
                     vacancy["url"], vacancy["snippet"]["responsibility"])
                )

    conn.commit()
    conn.close()
