import json
import os
from core.application_data import ApplicationData
from core.command_factory import CommandFactory

USERS_FILE = "users.json"


class ApplicationData:
    def __init__(self):
        self.users = self.load_users()
        self.logged_in_user = None

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
        if username in self.users and self.users[username]["password"] == password:
            self.logged_in_user = username
            return True
        return False

    def logout(self):
        self.logged_in_user = None


def main():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    print("Welcome to the Logistics Console Application!")

    while True:
        print("\nPlease select an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if app_data.login(username, password):
                print("Login successful!")

                while True:
                    print("\nLogged in as:", username)
                    print("\nPlease select an option:")
                    print("1. Register Employee")
                    print("2. Create Delivery Package")
                    print("3. Create Delivery Route")
                    print("4. View Information About Route")
                    print("5. Search for Route")
                    print("6. Logout")
                    print("7. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        cmd_factory.create("regiseremployee").execute()
                    elif choice == "2":
                        start_location = input("Enter the start location: ")
                        end_location = input("Enter the end location: ")
                        weight_kg = input("Enter the weight in kilograms: ")
                        contact_information = input("Enter the contact information: ")
                        cmd_factory.create("createdeliverypackage").execute(
                            [start_location, end_location, weight_kg, contact_information])
                    elif choice == "3":
                        routes = input("Enter route cities: ").split()
                        departure_date = input("Enter departure date (YYYY-MM-DD): ")
                        departure_time = input("Enter departure time (HH:MM): ")
                        route_info = cmd_factory.create("createdeliveryroute").execute(
                            [routes, departure_date, departure_time])
                        print(f"Route created successfully:\n {route_info}")
                    elif choice == "4":
                        route_id = input("Enter the route ID: ")
                        cmd_factory.create("viewinformationaboutroute").execute([route_id])
                    elif choice == "5":
                        cmd_factory.create("searchforroute").execute()
                    elif choice == "6":
                        app_data.logout()
                        print("Logged out successfully!")
                        break
                    elif choice == "7":
                        print("Exiting the application. Goodbye!")
                        return
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "2":
            username = input("Enter your desired username: ")
            if username in app_data.users:
                print("Username already taken. Please try another one.")
                continue

            password = input("Enter your desired password: ")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            position = input("Enter your position: ")

            if app_data.register_user(username, password, first_name, last_name, position):
                print("User created successfully!")
            else:
                print("Failed to create user. Username may already exist.")

        elif choice == "3":
            print("Exiting the application. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
