from enum import unique
from commands.helper_command.base_command import BaseCommand
from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from models.employee_role import EmployeeRole

class ViewInformationAboutRouteCommand(BaseCommand):

    def __init__(self,params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)
        employee = self._app_data.logged_in_employee
        if employee.employee_role != EmployeeRole.MANAGER:
            return "Error: Only Managers are allowed to view route information."

        route_id = super()._try_parse_int(params[0])
        try:
            route = self._app_data.find_route_by_id(route_id)
        except ValueError as ve:
            return f"\nError: {str(ve)}"

        assigned_vehicle = route.assigned_vehicle.vehicle_id if route.assigned_vehicle else 'None'

        return (
                f"\nRoute ID: {route.route_id}\n"
                f"Path: {' -> '.join(route.path)}\n"
                f"Total Distance: {route.distance} km\n"
                f"Assigned Vehicle: \n{assigned_vehicle}\n"
                "----------------------"
            )

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 1


