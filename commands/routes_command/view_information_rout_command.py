from commands.helper_command.base_command import BaseCommand
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
        route = self._app_data.find_route_by_id(route_id)
        return str(route)

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:

        return 1


