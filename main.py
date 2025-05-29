from src.config import config
from src.db_manager import DBManager
from src.utils import save_data_to_database, create_database
from src.interaction_api import get_list_employers


def main():
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
        "3910342"
    ]
    params = config()
    data = get_list_employers(company_ids)

    create_database("employees", params)
    save_data_to_database(data, "employees", params)

    emp = DBManager(params, "employees")
    emp.get_companies_and_vacancies_count()
    emp.get_all_vacancies()
    emp.get_avg_salary()
    emp.get_vacancies_with_higher_salary()
    emp.vacancies_with_keyword("Автомеханик")
    emp.close()




if __name__ == "__main__":
    main()
