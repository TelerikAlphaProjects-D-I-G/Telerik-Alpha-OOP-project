from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData

class ViewInformationAboutTruck(BaseCommand):
    def __init__(self,params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        truck_id = super()._try_parse_int(params[0])
        truck = self._app_data.find_truck_by_id(truck_id)

        if truck == "Truck not found":
            return f"Error: Truck with ID {truck_id} not found."

        return str(truck)

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 1