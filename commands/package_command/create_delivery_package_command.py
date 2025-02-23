from commands.helper_command.base_command import BaseCommand
# from models.package import Package
from core.application_data import ApplicationData
from commands.helper_command.validate_params_helpers_command import try_parse_int


class CreateDeliveryPackageCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        unique_id

        unique_id, start_location, end_location, weight_kg, contact_information = params

        try:
            unique_id = try_parse_int(unique_id)
            if unique_id is None:
                raise ValueError("Invalid type for ID, must be a number")

            weight_kg = try_parse_int(weight_kg)
            if weight_kg is None:
                raise ValueError("Invalid value for weight, must be a number.")

            # If everything is valid, create the package
            self._app_data.create_package(unique_id, start_location, end_location, weight_kg, contact_information)

            return (f"Your package has been successfully created.\n"
                    f" ID: {unique_id}\n"
                    f" Weight: {weight_kg} kg\n")

        except ValueError as e:
            return f"Error: {e}"

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 4