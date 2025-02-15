from commands.base_command import BaseCommand
from commands.create_delivery_route_command import CreateDeliveryRouteCommand
from core.application_data import ApplicationData
from models.route_matrix import Routes
from models.vehicles import Vehicles
from models.all_routes import AllRoutes
from storage_data.storage_trucks import TRUCKS
from commands.validate_params_helpers_command import validate_params_count
class AssignFreeTruckCommand(BaseCommand):

    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        truck_id, route_id = params
        route = self._app_data.find_route_by_id(route_id)
        if not route:
            return f'Error route with id {route_id} not found'
