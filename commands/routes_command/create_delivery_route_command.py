from commands.helper_command.base_command import BaseCommand
from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from models.route_matrix import Route
from datetime import datetime, timedelta, timezone


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        cities = params[:-2]
        departure_date_str = params[-2]
        departure_time_str = params[-1]
        route_id = Route.routes_id_counter


        departure_datetime_str = f"{departure_date_str} {departure_time_str}"

        try:

            departure_time = datetime.strptime(departure_datetime_str, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
        except ValueError:
            return "Error: Invalid departure time format. Please use 'YYYY-MM-DD HH:MM'."


        if departure_time < datetime.now(timezone.utc):
            return "❌ Error: Departure time cannot be in the past."

        try:
            total_distance, stop_distances = Route.calculate_total_distance(cities)
        except ValueError as ve:
            return f"\nError: {str(ve)}"

        try:
            new_route = self._app_data.create_route(cities, departure_time)
        except ValueError as ve:
            return f"\nError creating route: {str(ve)}"

        arrival_times = new_route.get_arrival_times()

        formatted_route = ' → '.join([f"{city} (Arrival at {arrival_time})" for city, arrival_time in zip(cities, arrival_times)])

        return (f"\n✅ Route created successfully with ID {new_route.route_id}:\n"
                f"🛤️ Route path: {formatted_route}\n"
                f"📏 Total distance: {total_distance} km")

    def _requires_login(self) -> bool:
        return True


