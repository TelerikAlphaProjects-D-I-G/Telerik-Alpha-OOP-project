import time
from datetime import datetime, timedelta

from commands.package_command.assign_delivery_package_command import AssignDeliveryPackageCommand
from core.application_data import ApplicationData
from commands.helper_command.base_command import BaseCommand
from commands.helper_command.validate_params_helpers_command import try_parse_int
from package_status import PackageStatus


class StartMovementTruckCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        truck_id = params[0]
        truck = self._app_data.find_truck_by_id(truck_id)
        print(f"Truck {truck_id} started delivered")
        delivered_count = 0
        for package in self._app_data.packages:
            if package.package_status == PackageStatus.IN_TRANSIT:
                package.set_status(PackageStatus.DELIVERED)
                delivered_count += 1
            print(f"Truck {truck_id} in transit...")
            time.sleep(2)
        if delivered_count > 0:
            return f"{delivered_count} package have been successfully delivered by Truck {truck_id}!"
        else:
            return f"📦 All packages were already delivered."

