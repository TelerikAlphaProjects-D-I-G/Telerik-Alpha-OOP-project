from datetime import datetime, timedelta
from models.vehicles import Vehicles

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

    SYD1 = ('Sydney', 'Sydney')
    MEL1 = ('Melbourne', 'Melbourne')
    ADL1 = ('Adelaide', 'Adelaide')
    PER1 = ('Perth', 'Perth')
    BRI1 = ('Brisbane', 'Brisbane')
    ASP1 = ('Alice Springs', 'Alice Springs')
    DAR1 = ('Darwin', 'Darwin')


    DISTANCES = {
        SYD[0]: {MEL[0]: 877, ADL[0]: 1376, ASP[0]: 2762, BRI[0]: 909, DAR[0]: 3935, PER[0]: 4016},
        MEL[0]: {SYD[0]: 877, ADL[0]: 725, ASP[0]: 2255, BRI[0]: 1765, DAR[0]: 3752, PER[0]: 3509},
        ADL[0]: {SYD[0]: 1376, MEL[0]: 725, ASP[0]: 1530, BRI[0]: 1927, DAR[0]: 3027, PER[0]: 2785},
        ASP[0]: {SYD[0]: 2762, MEL[0]: 2255, ADL[0]: 1530, BRI[0]: 2993, DAR[0]: 1497, PER[0]: 2481},
        BRI[0]: {SYD[0]: 909, MEL[0]: 1765, ADL[0]: 1927, ASP[0]: 2993, DAR[0]: 3426, PER[0]: 4311},
        DAR[0]: {SYD[0]: 3935, MEL[0]: 3752, ADL[0]: 3027, ASP[0]: 1497, BRI[0]: 3426, PER[0]: 4025},
        PER[0]: {SYD[0]: 4016, MEL[0]: 3509, ADL[0]: 2785, ASP[0]: 2481, BRI[0]: 4311, DAR[0]: 4025}

    }
    DISTANCES_FULL = {
        SYD1[0]: {MEL1[0]: 877, ADL1[0]: 1376, ASP1[0]: 2762, BRI1[0]: 909, DAR1[0]: 3935, PER1[0]: 4016},
        MEL1[0]: {SYD1[0]: 877, ADL1[0]: 725, ASP1[0]: 2255, BRI1[0]: 1765, DAR1[0]: 3752, PER1[0]: 3509},
        ADL1[0]: {SYD1[0]: 1376, MEL1[0]: 725, ASP1[0]: 1530, BRI1[0]: 1927, DAR1[0]: 3027, PER1[0]: 2785},
        ASP1[0]: {SYD1[0]: 2762, MEL1[0]: 2255, ADL1[0]: 1530, BRI1[0]: 2993, DAR1[0]: 1497, PER1[0]: 2481},
        BRI1[0]: {SYD1[0]: 909, MEL1[0]: 1765, ADL1[0]: 1927, ASP1[0]: 2993, DAR1[0]: 3426, PER1[0]: 4311},
        DAR1[0]: {SYD1[0]: 3935, MEL1[0]: 3752, ADL1[0]: 3027, ASP1[0]: 1497, BRI1[0]: 3426, PER1[0]: 4025},
        PER1[0]: {SYD1[0]: 4016, MEL1[0]: 3509, ADL1[0]: 2785, ASP1[0]: 2481, BRI1[0]: 4311, DAR1[0]: 4025}

    }

    def __init__(self, start_location, end_location):
        self.star_location = start_location
        self.end_location = end_location
        # self.stops = stops
        # self.departure_time = departure_time
        self.route_id = Routes.routes_id_counter
        Routes.routes_id_counter += 1
        self.assigned_vehicle = None

    @staticmethod
    def my_distance(start, end):
        if start in Routes.DISTANCES and end in Routes.DISTANCES[start]:
            return Routes.DISTANCES[start][end]

        if start in Routes.DISTANCES_FULL and end in Routes.DISTANCES_FULL[start]:
            return Routes.DISTANCES_FULL[start][end]

        raise ValueError('Invalid distance')

    @staticmethod
    def time_needed(start, end):
        distance = Routes.my_distance(start, end)
        if distance is None:
            return "Invalid route"
        travel_time = distance / Routes.AVERAGE_SPEED
        return timedelta(hours= travel_time)



    def assign_vehicle(self, vehicle_id):
        vehicle = Vehicles(vehicle_id)

        if self.assigned_vehicle is None:
            self.assigned_vehicle = vehicle
            return True
        return False

    @staticmethod
    def route_distance(routes):
        total_distance = 0
        for i in range(len(routes[0:-1]) - 1):
            current_city = routes[0:-1][i]
            next_city = routes[0:-1][i + 1]
            distance = Routes.my_distance(current_city, next_city)
            if distance is None:
                raise ValueError
            total_distance += distance

        return total_distance

    def __str__(self):
        return (f"Route id: {self.route_id}\n"
                f"Start location: {self.star_location}\n"
                # f"Additional stops: {self.stops}\n"
                f"End location: {self.end_location}\n"
                f"Assigned vehicle: {self.assigned_vehicle.vehicle_id}")

#print(Routes.my_distance('SYD',"MEL"))
#print(Routes.my_distance('Sydney', 'Melbourne'))
#print(Routes.time_needed('Sydney', 'Melbourne'))
#print(Routes.time_needed('SYD', 'MEL'))

route = Routes('SYD', 'ADL')
route.assign_vehicle(1001)
#print(route)
#print(Routes.time_needed('Sydney', 'Melbourne')) #does not work

