from datetime import datetime, timedelta
from models.vehicles import Vehicles
class Route:

    routes_lst = []
    routes_id_counter = 1
    TIME_SCALE = 10000
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

    def __init__(self, start_location, end_location, additional_stops = None, departure_time = None):
        self.start_location = start_location
        self.end_location = end_location
        self.additional_stops = additional_stops
        self.end_location = end_location
        self.departure_time = departure_time
        self.route_id = Route.routes_id_counter
        Route.routes_id_counter += 1
        self.assigned_vehicle = None

    @staticmethod
    def valid_distances(*all_stops):
        distances = Route.DISTANCES
        distances_full_name = Route.DISTANCES_FULL
        expanded_stops = [stop for sublist in all_stops for stop in (sublist if isinstance(sublist, list) else [sublist])]
        invalid_stops = [stop for stop in expanded_stops if stop not in distances and stop not in distances_full_name]

    @staticmethod
    def time_needed(start, end):
        distance = Route.calculate_total_distance(start, end)
        if distance is None:
            return "Invalid route"
        travel_time = distance / Route.AVERAGE_SPEED
        return timedelta(hours= travel_time)

    def assign_vehicle(self, vehicle_id):
        vehicle = Vehicles(vehicle_id)

        if self.assigned_vehicle is None:
            self.assigned_vehicle = vehicle
            return True
        return False

    def calculate_total_distance(*all_stops):
        Route.valid_distances(*all_stops)

        distances = Route.DISTANCES
        distances_full_name = Route.DISTANCES_FULL
        total_distance = 0

        expanded_stops = list(all_stops[0])

        stop_distances = []

        for i in range(len(expanded_stops) - 1):
            start = expanded_stops[i]
            end = expanded_stops[i + 1]
            city_distances = distances.get(start, distances_full_name)

            if end in city_distances:
                distance = city_distances[end]
                total_distance += distance
                stop_distances.append(f"{start} → {end}: {distance} km")
            else:
                raise ValueError(f"Distance between {start} and {end} is not available.")

        return total_distance, stop_distances

    def get_arrival_times(self):
        arrival_times = []
        current_time = self.departure_time

        path = [self.start_location] + self.additional_stops + [self.end_location]

        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]

            distance = Route.DISTANCES[start][end]
            travel_time = distance / Route.AVERAGE_SPEED
            current_time += timedelta(hours=travel_time)
            arrival_str = current_time.strftime("%b %dth %H:%M") + "h"
            arrival_times.append((end, arrival_str))
        return arrival_times


    def __str__(self):
        return (f"Route id: {self.route_id}\n"
                f"Start location: {self.start_location}\n"
                f"End location: {self.end_location}\n"
                f"Assigned vehicle: {self.assigned_vehicle.vehicle_id}")



