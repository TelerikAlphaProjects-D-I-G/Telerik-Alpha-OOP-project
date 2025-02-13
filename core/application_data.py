from models.package import Package
from models.route_matrix import Routes
from models.vehicles import Vehicles


class ApplicationData:

    def __init__(self):
        self._packages = []
        self.vehicles = []
        self.create_trucks()
        self.routes = []

    @property
    def packages(self):
        return self._packages

    def create_trucks(self):
        for truck_id in range(1001,1011):
            vehicle = Vehicles("Scania",truck_id)
            self.vehicles.append(vehicle)
        for truck_id in range(1011,1025):
            vehicle = Vehicles("Man", truck_id)
            self.vehicles.append(vehicle)
        for truck_id in range(1026,1040):
            vehicle = Vehicles("Actros",truck_id)
            self.vehicles.append(vehicle)

    def count_vehicles_on_road(self):
        vehicles_scania = 0
        vehicle_man = 0
        vehicles_actros = 0
        for vehicle in self.vehicles:
            if not vehicle.is_available:
                vehicles_scania += 1
        return f"Vehicles on road:{vehicles_scania}"


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

    def find_truck_by_id(self,unique_id):
        for truck in self.vehicles:
            if unique_id == truck.vehicle_id:
                return truck
        return "Truck not found"

    def find_route_by_id(self,route_id: int) -> Routes:
        for route in self.routes:
            if route_id == route.route_id:
                return route
        raise ValueError("Route not found")

    # def new_route(self,route):
    #     self.routes.append(route)



app_data = ApplicationData()

print(app_data.count_vehicles_on_road())