from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.route_matrix import Routes


class CreateDeliveryRouteCommand(BaseCommand):

    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self, params):
        test_route = Routes.route_distance(params)
        route_id = Routes.route_id
        all_routes = params
        new_route = self._app_data.create_route(all_routes)
        return f"Total distance: {test_route} km {test_route.route_id}"
        #return "Route is created. You can view route with command: CurrentRoutes"

    def _requires_login(self) -> bool:
        return True


