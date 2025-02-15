from commands.helper_command.base_command import BaseCommand
from models.route_matrix import Routes
from core.application_data import ApplicationData


class SearchForRouteCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        start, end = params

        try:
            distance = Routes.my_distance(start, end)
            time_needed = Routes.time_needed(start, end)
            return (f'Route from {start} to {end}:\n'
                    f' Distance: {distance} km\n'
                    f' Estimated Travel Time: {time_needed}')

        except ValueError:
            return f'Error: Invalid route between {start} and {end}.'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2
