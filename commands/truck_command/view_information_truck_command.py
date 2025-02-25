from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData
from commands.helper_command.validate_params_helpers_command import try_parse_int
class ViewInformationAboutTruck(BaseCommand):
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)
        # unique_id = try_parse_int(params[1])
        truck_id = super()._try_parse_int(params[0])
        truck = self._app_data.find_truck_by_id(truck_id)
        # package = self._app_data.find_package_by_id(unique_id)
        # truck.assign_package(package)
        if truck == "Truck not found":
            return f"\nError: Truck with ID {truck_id} not found."

        return f'\n{str(truck)}'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2