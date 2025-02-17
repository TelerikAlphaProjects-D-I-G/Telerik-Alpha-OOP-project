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
        "SYD": {"MEL": 877, "ADL": 1376, "ASP": 2762, "BRI": 909, "DAR": 3935, "PER": 4016},
        "MEL": {"SYD": 877, "ADL": 725, "ASP": 2255, "BRI": 1765, "DAR": 3752, "PER": 3509},
        "ADL": {"SYD": 1376, "MEL": 725, "ASP": 1530, "BRI": 1927, "DAR": 3027, "PER": 2785},
        "ASP": {"SYD": 2762, "MEL": 2255, "ADL": 1530, "BRI": 2993, "DAR": 1497, "PER": 2481},
        "BRI": {"SYD": 909, "MEL": 1765, "ADL": 1927, "ASP": 2993, "DAR": 3426, "PER": 4311},
        "DAR": {"SYD": 3935, "MEL": 3752, "ADL": 3027, "ASP": 1497, "BRI": 3426, "PER": 4025},
        "PER": {"SYD": 4016, "MEL": 3509, "ADL": 2785, "ASP": 2481, "BRI": 4311, "DAR": 4025}
    }

    DISTANCES_FULL = {
        "Sydney": {"Melbourne": 877, "Adelaide": 1376, "Alice Springs": 2762, "Brisbane": 909, "Darwin": 3935,
                   "Perth": 4016},
        "Melbourne": {"Sydney": 877, "Adelaide": 725, "Alice Springs": 2255, "Brisbane": 1765, "Darwin": 3752,
                      "Perth": 3509},
        "Adelaide": {"Sydney": 1376, "Melbourne": 725, "Alice Springs": 1530, "Brisbane": 1927, "Darwin": 3027,
                     "Perth": 2785},
        "Alice Springs": {"Sydney": 2762, "Melbourne": 2255, "Adelaide": 1530, "Brisbane": 2993, "Darwin": 1497,
                          "Perth": 2481},
        "Brisbane": {"Sydney": 909, "Melbourne": 1765, "Adelaide": 1927, "Alice Springs": 2993, "Darwin": 3426,
                     "Perth": 4311},
        "Darwin": {"Sydney": 3935, "Melbourne": 3752, "Adelaide": 3027, "Alice Springs": 1497, "Brisbane": 3426,
                   "Perth": 4025},
        "Perth": {"Sydney": 4016, "Melbourne": 3509, "Adelaide": 2785, "Alice Springs": 2481, "Brisbane": 4311,
                  "Darwin": 4025}
    }
    def __init__(self, start_location,additional_stops, end_location):
        self.star_location = start_location
        self.end_location = end_location
        self.additional_stops = additional_stops
        # self.departure_time = departure_time
        self.route_id = Routes.routes_id_counter
        Routes.routes_id_counter += 1
        self.assigned_vehicle = None
    #     NEW
    @staticmethod
    def valid_distances(*all_stops):
        distances = Routes.DISTANCES
        distances_full_name = Routes.DISTANCES_FULL
        expanded_stops = []
        for stop in all_stops:
            if isinstance(stop, list):
                expanded_stops.extend(stop)
            else:
                expanded_stops.append(stop)
        for stop in expanded_stops:
            if stop not in distances and stop not in distances_full_name:
                raise ValueError(f"Invalid stop: {stop}")

        return "All distances are valid"

        # if all_stops[0] not in Routes.DISTANCES or all_stops[0:-1] not in Routes.DISTANCES:
        #     return Routes.DISTANCES[all_stops]
        # raise ValueError('Invalid distance')
        # if all_stops[0] not in Routes.DISTANCES_FULL and all_stops[-1] not in Routes.DISTANCES_FULL[all_stops[0]]:
        #     # return Routes.DISTANCES[all_stops[0:-1]]
        #     raise ValueError('Invalid distance')

    @staticmethod
    def time_needed(start, end):
        distance = Routes.calculate_total_distance()
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

    def calculate_total_distance(*all_stops):
        Routes.valid_distances(*all_stops)
        distances = Routes.DISTANCES
        distances_full_name = Routes.DISTANCES_FULL
        total_distance = 0
        for i in range(len(all_stops) - 1):
            start = all_stops[i]
            end = all_stops[i + 1]
            city_distances = distances.get(start, distances_full_name)
            if end in city_distances:
                total_distance += city_distances[end]
            else:
                raise ValueError(f"Distance between {start} and {end} is not available.")
        return total_distance

    # @staticmethod
    # def route_distance(*routes):
    #     total_distance = 0
    #     for i in range(len(routes)-1):
    #         current_city = routes[i]
    #         next_city = routes[i + 1]
    #         distance = Routes.valid_distances(current_city, next_city)
    #         if distance is None:
    #             raise ValueError
    #         total_distance += distance
    #
    #     return total_distance

    def __str__(self):
        return (f"Route id: {self.route_id}\n"
                f"Start location: {self.star_location}\n"
                # f"Additional stops: {self.stops}\n"
                f"End location: {self.end_location}\n"
                f"Assigned vehicle: {self.assigned_vehicle.vehicle_id}")

# print(Routes.valid_distances("SYD","PER"))
print(Routes.calculate_total_distance("SYD","MEL","ADL","PER"))
# print(Routes.my_distance('Sydney', 'Melbourne'))
#print(Routes.time_needed('Sydney', 'Melbourne'))
#print(Routes.time_needed('SYD', 'MEL'))

# route = Routes('SYD', 'ADL')
# route.assign_vehicle(1001)
#print(route)
#print(Routes.time_needed('Sydney', 'Melbourne')) #does not work

