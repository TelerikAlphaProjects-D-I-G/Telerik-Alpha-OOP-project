from models.package import Package
from models.package_status import PackageStatus
from models.route_matrix import Route
from models.vehicles import Vehicles
from models.employee import Employee
from models.employee import EmployeeRole
from storage_data.storage_trucks import TRUCKS
import json
import os
USERS_FILE = "users.json"
class ApplicationData:

    def __init__(self):
        self._packages = []
        self.vehicles = []
        self._employees = self.load_users_from_json()
        self._logged_employee = None
        self.routes = []
        self._add_vehicles_to_vehicles_list()
        self.users = self.load_users()
        self.logged_in_user = None
        # self.package_id_count = Package.package_id_count

    def _add_vehicles_to_vehicles_list(self):
        for truck_id, truck_data in TRUCKS.items():
            vehicle = Vehicles(truck_id)
            self.vehicles.append(vehicle)

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
        return package

    def get_package(self,package_id):
        return self.packages.get(package_id)

    def create_package(self, start_location, end_location, weight_kg, contact_information) ->Package:
        package = Package(start_location, end_location, weight_kg, contact_information)
        self._packages.append(package)
        return package

    def find_package_by_id(self, package_id_count) -> Package:
        for id in self._packages:
            if package_id_count == id.package_id_count:
                return id
        return None

    def find_truck_by_id(self, vehicle_id: int):
        for truck in self.vehicles:
            if vehicle_id == truck.vehicle_id:
                return truck
        return "Truck not found"

    def find_route_by_id(self,route_id: int) -> Route:
        for route in self.routes:
            if route.route_id == route_id:
                return route
        raise ValueError("Route not found")

    def create_route(self, routes, departure_time) -> Route:
        if len(routes) <= 1:
            raise ValueError("Invalid route")

        total_distance, _ = Route.calculate_total_distance(routes)

        new_route = Route(
            start_location=routes[0],
            additional_stops=routes[1:-1],
            end_location=routes[-1],
            departure_time=departure_time
        )
        new_route.path = routes
        new_route.distance = total_distance

        arrival_times = new_route.get_arrival_times()

        formatted_stops = []
        for i in range(len(routes)):
            stop_info = f"{routes[i]} (Arrival at {arrival_times[i] if i < len(arrival_times) else 'N/A'})"
            formatted_stops.append(stop_info)

        self.routes.append(new_route)

        route_details = (
            f"Route ID: {new_route.route_id}\n"
            f"Path: {' → '.join(formatted_stops)}\n"
            f"Total Distance: {total_distance} km\n"
            f"Departure Time: {departure_time}\n"
            f"----------------------\n"
        )


        with open("routes_log.txt", "a", encoding="utf-8") as file:
            file.write(route_details)

        self.routes.append(new_route)
        return new_route



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
        if self._logged_employee is None:
            raise ValueError("No employee")
        return self._logged_employee

    def has_logged_in_employee(self):
        return self.logged_in_user is not None

    def login(self, employee: Employee):
        self.logged_in_user = employee

    def logout(self):
        self.logged_in_user = None

    def find_employee_by_username(self, username: Employee) -> Employee:
        for employee in self._employees:
            if username == employee.username:
                return employee
        raise ValueError("Wrong username!")

    def print_routes(self):
        return self.routes

    def search_routes(self, start_location, end_location):
        matching_routes = []
        seen_routes_id = set()
        for route in self.routes:
            if start_location in route.path and end_location in route.path:
                start_index = route.path.index(start_location)
                end_index = route.path.index(end_location)
                if start_index < end_index and route.route_id not in seen_routes_id:
                    matching_routes.append(route)
                    seen_routes_id.add(route.route_id)
        return matching_routes




    def load_users_from_json(self):
        with open("users.json", "r") as file:
            users_data = json.load(file)
        employees = []
        for username, data in users_data.items():
            employee = Employee(
                username = username,
                firstname = data["first_name"],
                lastname = data["last_name"],
                password = data["password"],
                employee_role = EmployeeRole.from_string(data["position"])
            )
            employees.append(employee)
        return employees

    def load_users(self):
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_users(self):
        """Save users to a JSON file."""
        with open(USERS_FILE, "w") as file:
            json.dump(self.users, file, indent=4)

    def register_user(self, username, password, first_name, last_name, position):
        """Register a new user and save to file."""
        if username in self.users:
            return False  # Username already exists
        self.users[username] = {
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }
        self.save_users()
        return True

    def find_employee_by_username(self, username):
        return self.users.get(username, None)

    def login(self, username, password):
        for employee in self._employees:
            if employee.username == username and employee.password == password:
                self._logged_employee = employee
                return True
        return False

    def logout(self):
        self.logged_in_user = None

    def find_trucks_in_city(self, city):
        trucks_in_city = []
        city = city.upper()

        for truck_id, truck in TRUCKS.items():
            if truck['city'] == city:
                truck_info = f"🚚 ID: {truck_id}, Model: {truck['model']}, Capacity: {truck['capacity']}kg, Range: {truck['max_range']}km"
                trucks_in_city.append(truck_info)

        return trucks_in_city

    def get_packages_by_status(self):
        all_on_pending = []
        for pack in self._packages:
            pending = PackageStatus.PENDING
            if pack.package_status == pending:
                all_on_pending.append(pack)
        return all_on_pending
