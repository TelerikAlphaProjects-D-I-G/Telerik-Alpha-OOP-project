from commands.base_command import BaseCommand
from commands.create_delivery_route_command import CreateDeliveryRouteCommand
from core.application_data import ApplicationData
from models.route_matrix import Routes
from models.vehicles import Vehicles
from models.all_routes import AllRoutes
from commands.validate_params_helpers_command import validate_params_count
class AssignFreeTruckCommand(BaseCommand):
    def __init__(self, params, app_data: ApplicationData):
        super().__init__(app_data)
        self._params = params
    #     new

    def execute(self):
        super().execute(self._params)
        route_id = self._params[0]
        route = self._app_data.find_route_by_id(route_id)
        if not route:
            return f"Error: Route with ID {route_id} not found."

        free_truck = self._app_data.get_free_truck()
        if not free_truck:
            return "Error: No free trucks available."


        route.assign_vehicle(free_truck)
        free_truck.assign_to_route(route)

        return f"Truck {free_truck.id} assigned to route {route_id}."

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 1
app_data = ApplicationData()
command = CreateDeliveryRouteCommand(["MEL","SYD","ADL",10],app_data)
comand = AssignFreeTruckCommand(1,app_data)
print(command.execute())