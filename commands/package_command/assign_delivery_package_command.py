from enum import unique

from PycharmProjects.test.tests.test_check_for_win import Routes
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

        unique_id, truck_id= params

        truck_id = try_parse_int(truck_id)
        if truck_id is None or truck_id not in TRUCKS:
            raise ValueError(f"Invalid truck ID: {truck_id}. Please provide a valid truck ID.")

        unique_id = try_parse_int(unique_id)
        package = self._app_data.find_package_by_id(unique_id)
        if package is None:
            raise ValueError(f"Package {unique_id} not found.")
        truck = Vehicles(truck_id)
        self._app_data.add_package(package)
        package.advance_status()
        truck.assign_package(package)
        return (
            f"Package ID: {unique_id}\n"
            f"Truck ID: {truck_id}\n"
            f"Package Status: {package.package_status}\n"
        )
    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 2


