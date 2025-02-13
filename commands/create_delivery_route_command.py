from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.all_routes import AllRoutes


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        self._app_data = app_data
        self._params = params

    def execute(self):
        test_route = AllRoutes.route_distance(self._params)
        all_routes = self._params
        new_route = self._app_data.create_route(all_routes)
        return f"{' -> '.join(new_route.cities)}\nTotal distance: {test_route} km"

    def _requires_login(self) -> bool:
        return True


