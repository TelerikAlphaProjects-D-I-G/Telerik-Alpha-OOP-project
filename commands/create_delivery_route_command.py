from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.all_routes import AllRoutes


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        test_route = AllRoutes.route_distance(params)
        all_routes = params
        new_route = self._app_data.create_route(all_routes)
        return f"{' -> '.join(new_route.cities)}\nTotal distance: {test_route} km"
        return "Route is created. You can view route with command: CurrentRoutes"

    def _requires_login(self) -> bool:
        return True


