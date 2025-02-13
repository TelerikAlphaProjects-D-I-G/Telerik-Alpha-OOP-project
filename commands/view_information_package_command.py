from core.application_data import ApplicationData
from commands.validate_params_helpers_command import validate_params_count, try_parse_int
from commands.base_command import BaseCommand


class ViewInformationAboutPackage(BaseCommand):

	def __init__(self, params, app_data: ApplicationData):
		super().__init__(app_data)


	def execute(self, params):
		super().execute(params)

		package_info_id = params[0]

		try:
			package_info_id = try_parse_int(package_info_id)
			if package_info_id is None:
				raise ValueError(f"'{package_info_id}' must be a number to proceed")
		except ValueError as ve:
			return f"Error: {str(ve)}"

		package = self._app_data.find_package_by_id(package_info_id)

		if package is None:
			return f"Error: No package found with ID {package_info_id}."

		return str(package)

	def _requires_login(self) -> bool:
		return True

	def _expected_params_count(self) -> int:
		return 1