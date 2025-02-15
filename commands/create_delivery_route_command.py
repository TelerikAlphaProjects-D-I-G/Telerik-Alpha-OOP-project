from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.route_matrix import Routes


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        try:
            total_distance = Routes.route_distance(params)
        except ValueError as ve:
            return f"Error: {str(ve)}"

        try:
            new_route = self._app_data.create_route(params)
        except ValueError as ve:
            return f"Error creating route: {str(ve)}"

        route_summary = f"Route created successfully with ID {new_route.route_id}:\n"
        route_summary += f"Route path: {' -> '.join(params)}\n"
        route_summary += f"Total distance: {total_distance} km"
        return route_summary

    def _requires_login(self) -> bool:
        return True


