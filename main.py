from src.config import config
from src.utils import save_data_to_database, create_database
from src.interaction_api import get_list_employers


def main():
    company_ids = [
        "8932785",
        "9451699",
        "1763330",
        "9553307",
        "1136246",
        "641905",
        "115257",
        "9746436",
        "11001750",
        "1332487"
    ]
    params = config()
    data = get_list_employers(company_ids)

    create_database("employers", params)
    save_data_to_database(data, "employers", params)


if __name__ == "__main__":
    main()
