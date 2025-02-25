from commands.helper_command.base_command import BaseCommand
from models.route_matrix import Route
from core.application_data import ApplicationData


class SearchForRouteCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        start_location, end_location = params[0], params[1]

        matching_routes = self._app_data.search_routes(start_location, end_location)

        if not matching_routes:
            return f'\nNo routes found from {start_location} to {end_location}.'

        routes_info = ''

        for route in matching_routes:
            arrival_times = route.get_arrival_times()

            formatted_route = ' → '.join([f"{city} (Arrival at {arrival_time})" for city, arrival_time in
                                          zip([route.start_location] + (route.additional_stops or []) +
                                              [route.end_location], arrival_times)])

            routes_info += (f"Route ID: {route.route_id}\n"
                            f"Departure: {route.departure_time.strftime('%b %dth %H:%M')}h\n"
                            f"Path: {formatted_route}\n--------------------\n")

        return f"\nMatching Routes:\n{routes_info}"

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2