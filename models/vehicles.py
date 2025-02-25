"""

SCANIA = ["Scania",42000,8000]
MAN = ["Man", 37000, 10000]
ACTROS = ["Actros",  26000,13000]

"""
import time

from commands.helper_command.validate_params_helpers_command import try_parse_int
from models.package_status import PackageStatus

from storage_data.storage_trucks import TRUCKS


class Vehicles:
    TIME_SCALE = 100000
    def __init__(self, vehicle_id):
        self.name = TRUCKS.get(vehicle_id, {}).get('model', 'uknown model')
        self.vehicle_id = vehicle_id
        self.capacity =TRUCKS.get(vehicle_id, {}).get('capacity', 0)
        self.max_range = TRUCKS.get(vehicle_id, {}).get('max_range', 0)
        self.current_city = TRUCKS.get(vehicle_id, {}).get('city', 'uknown city')
        self.current_load = 0
        self.is_available = True
        self.assigned_vehicle = None
        self.assigned_packages = []

    def assign_package(self, package):
        package.assign_to_truck(self)

    def assign_vehicle(self, vehicle_id):
        if self.assigned_vehicle is None:
            self.assigned_vehicle = vehicle_id
            return True
        return False

    def assign_to_work(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def work_done(self):
        self.is_available = True
        self.current_load = 0
        self.assigned_packages.clear()
        return True

    def __str__(self):
        assigned_packages_str = ", ".join(str(pkg.unique_id) for pkg in self.assigned_packages) if self.assigned_packages else "None"
        return (f'Name: {self.name}\n'
                f'Vehicle ID: {self.vehicle_id}\n'
                f'Capacity: {self.capacity} kg\n'
                f'Max Range: {self.max_range} km\n'
                f'Status: {"Available" if self.is_available else "Not Available"}\n'
                f'Current Load: {self.current_load} kg\n'
                f'Assigned Packages: {assigned_packages_str}\n'
                f"Current city: {self.current_city}")