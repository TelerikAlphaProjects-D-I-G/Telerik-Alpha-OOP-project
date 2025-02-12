from models.package import Package
from models.route_matrix import Routes
from models.vehicles import Vehicles


class ApplicationData:

    def __init__(self):
        self._packages = []
        self._truck =
    @property
    def packages(self):
        return self._packages

    def add_package(self,unique_id, start_location, end_location, weight_kg, contact_information)->Package :
        new_package = Package(unique_id,start_location,end_location,weight_kg,contact_information)
        self.packages[new_package.unique_id] = new_package
        return new_package.unique_id

    def get_package(self,package_id):
        return self.packages.get(package_id)

    def create_package(self, unique_id, start_location, end_location, weight_kg, contact_information) ->Package:
        package = Package(unique_id, start_location, end_location, weight_kg, contact_information)
        self._packages.append(package)
        return package

    def find_package_by_id(self, unique_id) -> Package:
        for id in self._packages:
            if id.unique_id == unique_id:
                return id

    def find_truck_by_id(self,unique_id): -> Vehicles:
        for id in self.
    # def assign_package_to_route(self,package_id, route_id, ):

