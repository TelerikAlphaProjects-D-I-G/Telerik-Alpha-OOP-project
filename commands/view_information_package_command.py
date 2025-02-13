from core.application_data import ApplicationData
from commands.validate_params_helpers_command import validate_params_count
from commands.base_command import BaseCommand
class ViewInformationAboutPackage(BaseCommand):

	def __init__(self, params, app_data: ApplicationData):
		super().__init__(app_data)
		validate_params_count(params, 1)
		self._params = params


	def execute(self):
		super().execute(self._params)
		package_info_id = super()._try_parse_int(self._params[0])
		package = self._app_data.find_package_by_id(package_info_id)

		return str(package)

	def _expected_params_count(self) -> int:
		return 1