from commands.helper_command.base_command import BaseCommand
from models.route_matrix import Route
from core.application_data import ApplicationData


class SearchForRouteCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self,params):
        super().execute(params)

        start_location, end_location = params[0], params[1]
        matching_routes = self._app_data.search_routes(start_location, end_location)

        if not matching_routes:
            return f'No routes found from {start_location} to {end_location}.'

        matches = 'Matching Routes:\n'+'\n'.join( f"- Route ID: {route.route_id}, Path: {' -> '.join(route.path)}" for route in matching_routes)

        return matches


    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2