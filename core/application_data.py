from models.package import Package
from models.route_matrix import Routes


class ApplicationData:

    def __init__(self):
        self._packages = {}

    @property
    def packages(self):
        return self._packages

    def add_package(self,unique_id, start_location, end_location, weight_kg, contact_information)->Package :
        new_package = Package(unique_id,start_location,end_location,weight_kg,contact_information)
        self.packages[new_package.unique_id] = new_package
        return new_package.unique_id

    def get_package(self,package_id):
        return self.packages.get(package_id)

    # def assign_package_to_route(self,package_id, route_id, ):

