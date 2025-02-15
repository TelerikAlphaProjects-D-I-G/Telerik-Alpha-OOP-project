from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData


class ViewLoggedInEmployeeCommand(BaseCommand):

    def __init__(self,params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        employee_username = params[0]

        employee = self._app_data.find_employee_by_username(employee_username)
        return str(employee)


    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:

        return 1
