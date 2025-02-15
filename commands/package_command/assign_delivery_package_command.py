from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData
from models.package_status import PackageStatus


class AssignDeliveryPackageCommand(BaseCommand):
    def __init__(self,params , app_data: ApplicationData):
        self.params = params
        super().__init__(app_data)


    def execute(self,params):
        if self.package.package_status != PackageStatus.PENDING:
            raise ValueError(f"Package {self.package.unique_id} is already proceed")

        if self.package.weight_kg > self.truck.capacity:
            raise ValueError(f"Package {self.package.unique_id} is too heavy for Truck {self.truck.truck_id}.")
        self.route.add_package(self.package)
        self.package.advance_status()

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0


#
# print(f"Package {self.package.unique_id} assigned to Truck {self.truck.truck_id} for delivery.")
# print(f"Package status updated to: {self.package.package_status}")

