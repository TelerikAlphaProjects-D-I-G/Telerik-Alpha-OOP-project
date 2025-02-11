from datetime import datetime, timedelta

class Routes:

    routes_lst = []
    routes_id_counter = 1

    AVERAGE_SPEED = 87

    SYD = ('SYD', 'Sydney')
    MEL = ('MEL', 'Melbourne')
    ADL = ('ADL', 'Adelaide')
    PER = ('PER', 'Perth')
    BRI = ('BRI', 'Brisbane')
    ASP = ('ASP', 'Alice Springs')
    DAR = ('DAR', 'Darwin')

    DISTANCES = {
        SYD[0]: {MEL[0]: 877, ADL[0]: 1376, ASP[0]: 2762, BRI[0]: 909, DAR[0]: 3935, PER[0]: 4016},
        MEL[0]: {SYD[0]: 877, ADL[0]: 725, ASP[0]: 2255, BRI[0]: 1765, DAR[0]: 3752, PER[0]: 3509},
        ADL[0]: {SYD[0]: 1376, MEL[0]: 725, ASP[0]: 1530, BRI[0]: 1927, DAR[0]: 3027, PER[0]: 2785},
        ASP[0]: {SYD[0]: 2762, MEL[0]: 2255, ADL[0]: 1530, BRI[0]: 2993, DAR[0]: 1497, PER[0]: 2481},
        BRI[0]: {SYD[0]: 909, MEL[0]: 1765, ADL[0]: 1927, ASP[0]: 2993, DAR[0]: 3426, PER[0]: 4311},
        DAR[0]: {SYD[0]: 3935, MEL[0]: 3752, ADL[0]: 3027, ASP[0]: 1497, BRI[0]: 3426, PER[0]: 4025},
        PER[0]: {SYD[0]: 4016, MEL[0]: 3509, ADL[0]: 2785, ASP[0]: 2481, BRI[0]: 4311, DAR[0]: 4025}

    }

    def __init__(self, start_location, end_location, stops, departure_time):
        self.star_location =start_location
        self.end_location = end_location
        self.stops = stops
        self.departure_time = departure_time
        self.route_id = Routes.routes_id_counter
        Routes.routes_id_counter += 1


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
        return timedelta(hours= travel_time)

# print(Routes.my_distance('ASP',"ADL"))
# print(Routes.time_needed('ASP',"ADL"))
#print(Routes.time_needed('Sydney', 'Melbourne')) #does not work