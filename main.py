from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine

# app_data = ApplicationData()
# cmd_factory = CommandFactory(app_data)
# engine = Engine(cmd_factory)
#
# engine.start()

class DeliveryApp:
    def __init__(self):
        self.routes = []
        self.packages = []

    def create_route(self):
        path = input("Enter route path (separated by spaces, e.g., SYD MEL PER): ").split()
        route_id = len(self.routes) + 1  # Unique ID
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

    def run(self):
        while True:
            print("\n🚛 Logistics Management System")
            print("1. Create Route")
            print("2. Create Package")
            print("3. Search for Routes")
            print("4. View Routes")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.create_route()
            elif choice == "2":
                self.create_package()
            elif choice == "3":
                self.search_routes()
            elif choice == "4":
                self.view_routes()
            elif choice == "5":
                print("👋 Exiting... Goodbye!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")

# Run the interactive app
if __name__ == "__main__":
    app = DeliveryApp()
    app.run()