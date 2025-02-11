"""
    SYD = ('SYD', 'Sydney')
    MEL = 'MEL', 'Melbourne'
    ADL = 'ADL', 'Adelaide'
    PER = 'PER', 'Perth'
    BRI = 'BRI', 'Brisbane'
    ASP = 'ASP', 'Alice Springs'
    DAR = 'DAR', 'Darwin'

"""
from datetime import datetime, timedelta

class Routes:
    LOCATION_MAPPING = {
        "Sydney": "SYD",
        "Melbourne": "MEL",
        "Adelaide": "ADL",
        "Perth": "PER",
        "Brisbane": "BRI",
        "Alice Springs": "ASP",
        "Darwin": "DAR"
    }

    AVERAGE_SPEED = 87

    DISTANCES = {
        "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
        "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
        "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
        "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
        "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
        "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
        "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}

    }

    @staticmethod
    def get_city_code(location_mapping):
        if location_mapping in Routes.LOCATION_MAPPING.keys():
            return Routes.LOCATION_MAPPING[location_mapping]
        return location_mapping


    @staticmethod
    def my_distance(start,end):
        start_code = Routes.get_city_code(start)
        end_code = Routes.get_city_code(end)
        if start_code not in Routes.DISTANCES or end_code not in Routes.DISTANCES:
            raise ValueError("Invalid distance")
        if start_code == end_code:
            return 0
        return  Routes.DISTANCES.get(start_code,{}).get(end_code)

    @staticmethod
    def time_needed(start, end):
        distance = Routes.my_distance(start, end)
        if distance is None:
            return "Invalid route"
        travel_time = distance / Routes.AVERAGE_SPEED
        return timedelta(hours= travel_time)

# print(Routes.my_distance('MEL',"Adelaide"))
#
# print(Routes.time_needed('Sydney', 'Melbourne'))


