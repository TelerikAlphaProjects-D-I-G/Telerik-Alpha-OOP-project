"""
    SYD = 'SYD', 'Sydney'
    MEL = 'MEL', 'Melbourne'
    ADL = 'ADL', 'Adelaide'
    PER = 'PER', 'Perth'
    BRI = 'BRI', 'Brisbane'
    ASP = 'ASP', 'Alice Springs'
    DAR = 'DAR', 'Darwin'

"""
from datetime import datetime, timedelta

class Routes:

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
    def my_distance(start,end):
        if start not in Routes.DISTANCES or end not in Routes.DISTANCES:
            raise ValueError("Invalid distance")
        if start == end:
            return 0
        return  Routes.DISTANCES.get(start,{}).get(end)

    @staticmethod
    def time_needed(start, end):
        distance = Routes.my_distance(start, end)
        if distance is None:
            return "Invalid route"
        travel_time = distance / Routes.AVERAGE_SPEED
        time_delta = timedelta(hours=travel_time)
        return str(time_delta).split(".")[0]
print(Routes.my_distance('ASP',"ADL"))

print(Routes.time_needed('SYD', 'MEL'))


