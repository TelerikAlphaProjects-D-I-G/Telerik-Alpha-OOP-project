from core.application_data import ApplicationData
from commands.helper_command.base_command import BaseCommand
from commands.user_command.login_command import LoginCommand
from commands.user_command.register_employee_command import RegisterEmployeeCommand
class PrintRoutes(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params=None):
        if not self._app_data.routes:
            return "No routes available."

        route_list = []
        for route in self._app_data.routes:
            route_list.append(
                f"Route ID: {route.route_id}\n"
                f"Path: {' -> '.join(route.path)}\n"
                f"Total Distance: {route.distance} km\n"
                f"Assigned Vehicle: {route.assigned_vehicle.vehicle_id if route.assigned_vehicle else 'None'}\n"
                "----------------------"
            )

        return "\n".join(route_list)

    def _requires_login(self) -> bool:
        return True