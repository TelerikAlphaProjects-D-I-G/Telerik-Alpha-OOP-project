from models.package import Package
from models.route_matrix import Routes
from models.vehicles import Vehicles
from models.employee import Employee


class ApplicationData:

    def __init__(self):
        self._packages = []
        self.vehicles = []
        self._employees = []
        self._logged_employee = None
        self.routes = []

    @property
    def packages(self):
        return self._packages

    def count_vehicles_on_road(self):
        vehicles_scania = 0
        vehicle_man = 0
        vehicles_actros = 0
        for vehicle in self.vehicles:
            if not vehicle.is_available:
                vehicles_scania += 1
        return f"Vehicles on road:{vehicles_scania}"


    def add_package(self,package)->Package :
        self._packages.append(package)

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
            if route.route_id == route_id:
                return route
        raise ValueError("Route not found")

    def create_route(self, routes) -> Routes:
        if len(routes) <= 1:
            raise ValueError("Invalid route")
        route = Routes.route_distance(routes)
        new_route = Routes(start_location = routes[0],additional_stops= routes[1:-1] , end_location = routes[-1])
        new_route.route_id = len(self.routes) + 1
        new_route.path = routes
        new_route_distance = route
        self.routes.append(new_route)
        return new_route

    # def new_route(self,route):
    #     self.routes.append(route)

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

    def find_employee_by_username(self, username: Employee) -> Employee:
        for employee in self._employees:
            if username == employee.username:
                return employee
        raise ValueError("Wrong username!")



# app_data = ApplicationData()
#
# print(app_data.count_vehicles_on_road())