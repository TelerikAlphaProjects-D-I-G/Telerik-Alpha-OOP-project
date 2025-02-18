from commands.helper_command.base_command import BaseCommand
from models.route_matrix import Routes
from core.application_data import ApplicationData


class SearchForRouteCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        super().execute(params)

        stops = params

        try:
            distance = Routes.valid_distances(stops)
            time_needed = Routes.time_needed(stops[0],stops[-1])
            return (f'Route from {stops[0]} to {stops[-1]}:\n'
                    f' Distance: {distance} km\n'
                    f' Estimated Travel Time: {str(time_needed).split('.')[0]}')

        except ValueError:
            return f'Error: Invalid route between {stops[0]} and {stops[-1]}.'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2
