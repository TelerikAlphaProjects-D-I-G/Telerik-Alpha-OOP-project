from commands.base_command import BaseCommand
from commands.create_delivery_route_command import CreateDeliveryRouteCommand
from core.application_data import ApplicationData
from models.route_matrix import Routes
from models.vehicles import Vehicles
from storage_data.storage_trucks import TRUCKS
from commands.validate_params_helpers_command import validate_params_count, try_parse_int


class AssignFreeTruckCommand(BaseCommand):

    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):

        truck_id, route_id = params


        truck_id = try_parse_int(truck_id)
        if truck_id is None or truck_id not in TRUCKS:
            raise ValueError(f"Invalid truck ID: {truck_id}. Please provide a valid truck ID.")

        route_id = try_parse_int(route_id)
        route = self._app_data.find_route_by_id(route_id)
        if route is None:
            raise ValueError(f"Route ID {route_id} not found.")

        truck = Vehicles(truck_id)

        if not truck.is_available:
            raise ValueError(f'Truck {truck_id} is not available.')

        truck.assign_to_work()

        route.assign_vehicle(truck)

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2






