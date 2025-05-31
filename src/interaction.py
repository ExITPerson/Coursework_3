from src.api_class import HeadHunterAPI
from src.config import config
from src.db_manager import DBManager
from src.utils import create_database, save_data_to_database


def user_interaction():
    company_ids = [
        "8932785",
        "1763330",
        "1136246",
        "641905",
        "115257",
        "9746436",
        "11001750",
        "1332487",
        "4538007",
        "3910342",
    ]

    params = config()
    data = HeadHunterAPI(company_ids).get_info()
    create_database("employees", params)
    save_data_to_database(data, "employees", params)

    try:

        user_input = int(
            input(
                "Какой результат вы хотели бы получить в выдаче (выберете цифру):\n"
                "1) Список всех компаний и кол-во вакансий.\n"
                "2) Список всех вакансий.\n"
                "3) Среднюю зарплату по вакансиям.\n"
                "4) Список всех вакансий с зарплатой выше среднего.\n"
                "5) Вакансии по ключевому слову.\n"
            )
        )

        emp = DBManager(params, "employees")

        if user_input == 1:
            result = emp.get_companies_and_vacancies_count()

            for company in result:
                print(
                    f"Компания: {company[1]}\n"
                    f"Кол-во открытых вакансий: {company[2]}\n"
                )

        elif int(user_input) == 2:
            result = emp.get_all_vacancies()

            for vacancy in result:
                print(
                    f"Компания: {vacancy[0]}\n"
                    f"Вакансия: {vacancy[1]}\n"
                    f"Зарплата: {vacancy[2] if vacancy[2] is not None else "Не указана"} руб.\n"
                    f"Ссылка на вакансию: {vacancy[3]}\n"
                )

        elif user_input == 3:
            result = emp.get_avg_salary()
            print(f"Средняя зарплата: {result[0]}\n")

        elif user_input == 4:

            result = emp.get_vacancies_with_higher_salary()
            for vacancy in result:
                print(
                    f"Название: {vacancy[2]}\n"
                    f"Город: {vacancy[3]}\n"
                    f"Зарплата: {vacancy[4] if vacancy[4] is not None else "Не указана"} руб.\n"
                    f"Ссылка: {vacancy[6]}\n"
                    f"Описание: {vacancy[7]}\n"
                )

        elif user_input == 5:

            input_key = str(input("Введите ключевое слово\n"))

            result = emp.get_vacancies_with_keyword(input_key)

            if len(result) != 0:
                for vacancy in result:
                    print(
                        f"Название: {vacancy[2]}\n"
                        f"Город: {vacancy[3]}\n"
                        f"Зарплата: {vacancy[4] if vacancy[4] is not None else "Не указана"} руб.\n"
                        f"Ссылка: {vacancy[6]}\n"
                        f"Описание: {vacancy[7]}\n"
                    )

            else:
                print("Вакансий по заданному ключу нет.")

        else:
            print("Вы ввели не правильный запрос, попробуйте снова")
            emp.close()
            user_interaction()

        emp.close()

    except ValueError:
        print("Введено не правильное значение, попробуйте заново\n")
        user_interaction()
