from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData
from models.employee import Employee


class LoginCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._throw_if_employee_logged_in()

        username, password = params

        employee = self._app_data.find_employee_by_username(username)
        if Employee.validate_password(password) != employee.password:
            raise ValueError('Wrong username or password!')
        else:
            self._app_data.login(employee)

            return f'Employee {employee.username} successfully logged in!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2