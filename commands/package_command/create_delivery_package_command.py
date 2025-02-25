from commands.helper_command.base_command import BaseCommand
# from models.package import Package
from core.application_data import ApplicationData
from commands.helper_command.validate_params_helpers_command import try_parse_int
from models.package import Package


class CreateDeliveryPackageCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        # unique_id = Package.package_id_counter

        start_location, end_location, weight_kg, contact_information = params

        try:
            weight_kg = try_parse_int(weight_kg)
            if weight_kg is None:
                raise ValueError("\nInvalid value for weight, must be a number.")


            new_package = self._app_data.create_package(start_location, end_location, weight_kg, contact_information)

            return (
    "\n✅ PACKAGE CREATED SUCCESSFULLY!\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"📦 Package ID : {new_package.package_id_count}\n"
    f"⚖️ Weight     : {weight_kg} kg\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
)

        except ValueError as e:
            return f"\nError: {e}"

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 4