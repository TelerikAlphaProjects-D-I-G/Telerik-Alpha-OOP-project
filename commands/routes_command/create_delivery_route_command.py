from commands.helper_command.base_command import BaseCommand
from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from models.route_matrix import Routes


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        cities = params[1:-1]
        route_id = params[-1]
        route_id = try_parse_int(route_id)
        try:
            total_distance = Routes.calculate_total_distance(params)
        except ValueError as ve:
            return f"Error: {str(ve)}"

        try:
            new_route = self._app_data.create_route(params)
        except ValueError as ve:
            return f"Error creating route: {str(ve)}"
        return (f"Route created successfully with ID {route_id}:\n"
        f"Route path: {' -> '.join(cities)}\n"
         f"Total distance: {total_distance} km")

    def _requires_login(self) -> bool:
        return True


