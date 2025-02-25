from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData

class FindTrucksInCityCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        city = params[0]
        trucks_in_city = self._app_data.find_trucks_in_city(city)

        if not trucks_in_city:
            return f"No trucks found in {city.upper()}."

        return f"\nTrucks in {city.upper()}:\n" + "\n".join(trucks_in_city) + "\n----------------------"

    def _requires_login(self) -> bool:
        return  False

    def  _expected_params_count(self) -> int:
        return 1