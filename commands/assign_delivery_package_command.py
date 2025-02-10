from commands.base_command import BaseCommand
from models.package_status import PackageStatus
from models.route_matrix import Routes
from models.package import Package


class AssignDeliveryPackageCommand:
    def __init__(self, package, route, truck):
        self.package = package
        self.route = route
        self.truck = truck

    def execute(self):
        if self.package.package_status != PackageStatus.PENDING:
            raise ValueError(f"Package {self.package.unique_id} is not in Pending status.")

        if self.package.weight_kg > self.truck.capacity:
            raise ValueError(f"Package {self.package.unique_id} is too heavy for Truck {self.truck.truck_id}.")
        self.route.add_package(self.package)
        self.package.advance_status()


        print(f"Package {self.package.unique_id} assigned to Truck {self.truck.truck_id} for delivery.")
        print(f"Package status updated to: {self.package.package_status}")

