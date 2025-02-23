from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from storage_data.storage_trucks import TRUCKS


# app_data = ApplicationData()
# cmd_factory = CommandFactory(app_data)
# engine = Engine(cmd_factory)
#
# engine.start()

class DeliveryApp:
    def __init__(self):
        self.routes = []
        self.packages = []
        self.employees = []

    def register_employee(self):
        name = input("Enter employee name: ")
        position_employee = input("Enter employee position: ")
        employee = {"name": name, "position employee": position_employee}
        self.employees.append(employee)
        print(f"Employee {name} (registered as {position_employee})")

    def create_route(self):
        path = input("Enter route path (separated by spaces, e.g., SYD MEL PER): ").split()
        route_id = len(self.routes) + 1
        route = {"route_id": route_id, "path": path}
        self.routes.append(route)
        print(f"✅ Route {route_id} created: {' -> '.join(path)}")

    def create_package(self):
        start = input("Enter package start location: ")
        end = input("Enter package destination: ")
        weight = input("Enter package weight (kg): ")
        contact = input("Enter contact name: ")
        package_id = len(self.packages) + 1
        package = {"id": package_id, "start": start, "end": end, "weight": weight, "contact": contact}
        self.packages.append(package)
        print(f"📦 Package {package_id} created from {start} to {end}, {weight}kg.")

    def assign_free_truck(self):
        pass

    def assign_delivery_package(self):
        pass

    def search_routes(self):
        start = input("Enter start location: ")
        end = input("Enter destination: ")
        matching_routes = [r for r in self.routes if start in r["path"] and end in r["path"]]
        if matching_routes:
            print("🔍 Matching Routes:")
            for r in matching_routes:
                print(f"- Route ID: {r['route_id']}, Path: {' -> '.join(r['path'])}")
        else:
            print("❌ No routes found.")

    def view_routes(self):
        if not self.routes:
            print("❌ No routes available.")
            return
        print("📍 Available Routes:")
        for r in self.routes:
            print(f"- Route {r['route_id']}: {' -> '.join(r['path'])}")

    def view_trucks(self):
        id_trucks = input("Enter truck's id: ")
        print("Available Trucks: ")
        id_trucks = int(id_trucks)
        truck = TRUCKS.get(id_trucks)
        print(
            f"🚛 Truck ID: {id_trucks}, "
            f"Model: {truck['model']}, "
            f"Capacity: {truck['capacity']}kg, "
            f"Max Range: {truck['max_range']}km, "
            f"Location: {truck['city']}")

    def view_packages(self):
        print("Available Packages: ")
        for package in self.packages:
            print(
                f"- Package ID: {package['id']},"
                f" From: {package['start']} -> To {package['end']},"
                f" Weight: {package['weight']}kg, "
                f"Contact: {package['contact']}")

    def run(self):
        while True:
            print("\n🚛 Logistics Management System")
            print("1. Register employee")
            print("2. Create Route")
            print("3. Create Package")
            print("4. Search for Routes")
            print("5. Assign Free Truck to Route")
            print("6. Assign Package to Truck")
            print("7. View Routes")
            print("8. View Trucks")
            print("9. View Package")
            print("10. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.register_employee()
            elif choice == "2":
                self.create_route()
            elif choice == "3":
                self.create_package()
            elif choice == "4":
                self.search_routes()
            elif choice == "5":
                self.assign_free_truck()
            elif choice == "6":
                self.assign_delivery_package()
            elif choice == "7":
                self.view_routes()
            elif choice == "8":
                self.view_trucks()
            elif choice == "9":
                self.view_packages()
            elif choice == "10":
                print("👋 Exiting... Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    app = DeliveryApp()
    app.run()