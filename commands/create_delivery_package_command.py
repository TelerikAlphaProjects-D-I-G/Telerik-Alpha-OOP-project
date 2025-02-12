from commands.base_command import BaseCommand
# from models.package import Package
from core.application_data import ApplicationData
from commands.validate_params_helpers_command import validate_params_count, try_parse_int

class CreateDeliveryPackageCommand:

    def __init__(self, params, app_data: ApplicationData):
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id = self._params[0]
        package_start_location = self._params[1]
        package_end_location = self._params[2]
        package_weight_kg = self._params[3]
        package_coninfo = self._params[4]
        try:
            package_weight_kg = try_parse_int(package_weight_kg)
        except:
            raise ValueError('Invalid type weight')
        self._app_data.create_package(package_id, package_start_location, package_end_location, package_weight_kg, package_coninfo)
        return f"Your package has been successfully created with ID {package_id}"