from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData
from models.vehicles import Vehicles
from storage_data.storage_trucks import TRUCKS
from commands.helper_command.validate_params_helpers_command import try_parse_int


class AssignFreeTruckCommand(BaseCommand):

    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):

        truck_id, route_id = params


        truck_id = try_parse_int(truck_id)
        try:
            if truck_id is None or truck_id not in TRUCKS:
                raise ValueError(f"Invalid truck ID: {truck_id}. Please provide a valid truck ID.")
        except ValueError as ve:
            return f"\nError: {str(ve)}"
        route_id = try_parse_int(route_id)
        try:
            route = self._app_data.find_route_by_id(route_id)
        except ValueError as ve:
            return f"\nError: {str(ve)}"

        if route is None:
            raise ValueError(f"Route ID {route_id} not found.")

        truck = Vehicles(truck_id)

        if not truck.is_available:
            raise ValueError(f'Truck {truck_id} is not available.')

        truck.assign_to_work()

        truck.assign_vehicle(truck_id)
        route.assigned_vehicle = truck

        return (
            f"\n🚛 Truck ID: {truck_id} (Status: {'Available' if truck.is_available else 'Assigned'})\n"
            f"🛣️ Route ID: {route.route_id}\n"
            f"🏙️ Path: {' -> '.join(route.path)}\n"
        )
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2
