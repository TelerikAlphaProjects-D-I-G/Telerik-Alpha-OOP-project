from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.employee_role import EmployeeRole

class RegisterEmployeeCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._throw_if_employee_logged_in()

        username, firstname, lastname, password, *rest = params

        if rest == []:
            employee_role = EmployeeRole.EMPLOYEE
        else:
            employee_role = EmployeeRole.from_string(rest[0])

        employee = self._app_data.create_employee_acc(username, firstname, lastname, password, employee_role)
        self._app_data.login(employee)

        return f'Employee {employee.username} registered successfully.'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 4