from enum import unique
from commands.helper_command.base_command import BaseCommand
from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from models.package_status import PackageStatus
from models.package import Package
from models.route_matrix import Route
from models.vehicles import Vehicles
from storage_data.storage_trucks import TRUCKS


class AssignDeliveryPackageCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)


    def execute(self, params):

        package_id_count, truck_id= params

        truck_id = try_parse_int(truck_id)
        try:
            if truck_id is None or truck_id not in TRUCKS:
                raise ValueError(f"\nInvalid truck ID: {truck_id}. Please provide a valid truck ID.")
        except ValueError as ve:
            return f"\nError: {str(ve)}"
        package_id_count = try_parse_int(package_id_count)
        package = self._app_data.find_package_by_id(package_id_count)
        if package is None:
            raise ValueError(f"\nPackage {package_id_count} not found.")
        truck = Vehicles(truck_id)
        if truck is None:
            raise ValueError(f"\nTruck with ID {truck_id} does not exist!")
        package.advance_status()
        truck.assign_package(package)
        return (
    "\n🚛 PACKAGE ASSIGNMENT DETAILS\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"📦 Package ID      : {package_id_count}\n"
    f"🚛 Truck ID        : {truck_id}\n"
    f"📌 Package Status  : {package.package_status}\n"
    f"📦 Assigned Package: {truck.current_load}\n"
    f"⚖️ Current Load    : {truck.current_load} / {truck.capacity} kg\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
)
    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2


