from core.application_data import ApplicationData
from commands.helper_command.validate_params_helpers_command import try_parse_int
from commands.helper_command.base_command import BaseCommand
from models.employee_role import EmployeeRole


class ViewInformationAboutPackage(BaseCommand):

	def __init__(self, params, app_data: ApplicationData):
		super().__init__(app_data)


	def execute(self, params):
		super().execute(params)

		employee = self._app_data.logged_in_employee
		if employee.employee_role not in [EmployeeRole.SUPERVISING_EMPLOYEE, EmployeeRole.MANAGER]:
			return '\nError: Only Supervisors and Managers have access to this data!'

		package_info_id = params[0]

		try:
			package_info_id = try_parse_int(package_info_id)
			if package_info_id is None:
				raise ValueError(f"'{package_info_id}' must be a number to proceed")
		except ValueError as ve:
			return f"\nError: {str(ve)}"

		package = self._app_data.find_package_by_id(package_info_id)

		if package is None:
			return f"\nError: No package found with ID {package_info_id}."

		return str(package)

	def _requires_login(self) -> bool:
		return False

	def _expected_params_count(self) -> int:
		return 1