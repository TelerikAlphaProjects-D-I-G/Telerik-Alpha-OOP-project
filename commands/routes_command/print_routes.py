from core.application_data import ApplicationData
from commands.helper_command.base_command import BaseCommand
from commands.user_command.login_command import LoginCommand
from commands.user_command.register_employee_command import RegisterEmployeeCommand
from models.employee_role import EmployeeRole


class PrintRoutes(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params=None):

        employee = self._app_data.logged_in_employee
        if employee.employee_role not in [EmployeeRole.MANAGER]:
            return '\nError: Only Managers have access to this data!'

        if not self._app_data.routes:
            return "\nNo routes available."

        route_list = []
        seen_routes_id = set()
        for route in self._app_data.routes:
            if route.route_id not in seen_routes_id:
                route_list.append(
                    f"\nRoute ID: {route.route_id}\n"
                    f"Path: {' -> '.join(route.path)}\n"
                    f"Total Distance: {route.distance} km\n"
                    f"Assigned Vehicle: {route.assigned_vehicle.vehicle_id if route.assigned_vehicle else 'None'}\n"
                    "----------------------"
                )
                seen_routes_id.add(route.route_id)

        return "\n".join(route_list)

    def _requires_login(self) -> bool:
        return True