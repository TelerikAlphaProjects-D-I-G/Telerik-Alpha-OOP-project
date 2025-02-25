from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData
from models.employee import Employee
from models.employee_role import EmployeeRole

class RegisterEmployeeCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._throw_if_employee_logged_in()

        username, password, firstname, lastname, role = params

        try:
            employee_role = EmployeeRole.from_string(role)
        except ValueError as ve:
            return f"\nError: {str(ve)}"

        try:
            employee = self._app_data.create_employee_acc(username, firstname, lastname, Employee.validate_password(password), employee_role)
        except ValueError as ve:
            return f"\nError: {str(ve)}"

        # Automatically log in the new employee
        self._app_data.login(employee.username, employee.password)

        return f"\nEmployee {employee.username} registered successfully as {employee_role}."

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 5