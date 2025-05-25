from src.interaction_api import get_list_employers

list_id = ["8932785",  "9451699", "1763330", "9553307", "1136246", "641905", "115257", "9746436", "11001750", "1332487"]


for empl_id in list_id:
    print(get_list_employers(empl_id))