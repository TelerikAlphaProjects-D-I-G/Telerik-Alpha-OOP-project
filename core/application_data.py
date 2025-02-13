from models.all_routes import AllRoutes
from models.package import Package
from models.route_matrix import Routes
from models.vehicles import Vehicles
from models.employee import Employee


class ApplicationData:

    def __init__(self):
        self._packages = []
        self.vehicles = []
        self.create_trucks()
        self.routes = []
        self._employees = []
        self._logged_employee = None

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
        return None

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

    def create_route(self, routes) -> AllRoutes:
        if len(routes) < 2:
            raise ValueError("Invalid route")
        route = AllRoutes.route_distance(routes)
        new_route = AllRoutes()
        new_route.cities = routes
        self.routes.append(new_route)
        return new_route

    def new_route(self,route):
        self.routes.append(route)

    @property
    def employees(self):
        return tuple(self._employees)

    def create_employee_acc(self, username, firstname, lastname, password, employee_role) -> Employee:
        if len([e for e in self._employees if e.username == username]) > 0:
            raise ValueError(f'User {username} already exist. Choose a different username!')

        employee = Employee(username, firstname, lastname, password, employee_role)
        self._employees.append(employee)
        return employee

    def find_employee_by_username(self, username: str) -> Employee:
        filtered = [employee for employee in self._employees if employee.username == username]
        if filtered == []:
            raise ValueError(f'There is no employee with username {username}.')
        return filtered[0]

    @property
    def logged_in_employee(self):
        if self.has_logged_in_employee:
            return self._logged_employee
        else:
            raise ValueError('There is no logged in employee.')

    def has_logged_in_employee(self):
        return self._logged_employee is not None

    def login(self, employee: Employee):
        self._logged_employee = employee

    def logout(self):
        self._logged_employee = None



app_data = ApplicationData()

print(app_data.count_vehicles_on_road())