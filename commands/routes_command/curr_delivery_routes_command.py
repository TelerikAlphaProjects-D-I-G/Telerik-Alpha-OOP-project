from commands.helper_command.base_command import BaseCommand
from commands.routes_command.create_delivery_route_command import CreateDeliveryRouteCommand
from core.application_data import ApplicationData
class CurrDeliveryRoutesCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params) -> CreateDeliveryRouteCommand:
        super().execute(params)
        all_routes = params
        new_route = self._app_data.create_route(all_routes)
        return f"{' -> '.join(new_route.cities)}\nTotal distance: {test_route} km"


    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:

        return 0