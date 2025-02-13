from commands.base_command import BaseCommand
# from models.package import Package
from core.application_data import ApplicationData
from commands.validate_params_helpers_command import validate_params_count, try_parse_int

class CreateDeliveryPackageCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)

        unique_id, start_location, end_location, weight_kg, contact_information = params
        try:
            unique_id = try_parse_int(unique_id)
        except:
            raise ValueError('Invalid type id')
        try:
            weight_kg = try_parse_int(weight_kg)
        except:
            raise ValueError('Invalid type weight')
        self._app_data.create_package(unique_id, start_location, end_location, weight_kg, contact_information)
        return f"Your package has been successfully created with ID {unique_id}"

    def _expected_params_count(self) -> int:
        return 5