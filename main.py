import json
import os

from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from models.package import Package


class Main:
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
                    print("1. Truck Commands")
                    print("2. Package Commands")
                    print("3. Route Commands")
                    print("4. Logout")
                    print("5. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print("\nTruck Commands:")
                        print("1. Assign Free Truck to Route")
                        print("2. View Truck Information")
                        print("3. Back to main menu")
                        truck_choice = input("Enter your choice: ")

                        if truck_choice == "1":
                            route_id = int(input("Enter ID route: "))
                            truck_id = int(input("Enter ID truck: "))
                            cmd = cmd_factory.create("assignfreetruck")
                            result = cmd.execute([truck_id, route_id])
                            print(result)

                        if truck_choice == "2":
                            truck_id = int(input("Enter ID truck: "))
                            cmd = cmd_factory.create("viewinformationabouttruck")
                            result = cmd.execute([truck_id])
                            print(result)

                        elif choice == "3":
                            continue

                        else:
                            print('Invalid choice. Please try again.')



                    elif choice == "2":
                        print("\nPackage Commands:")
                        print("1. Create Delivery Package")
                        print("2. View Information About Package")
                        print("3. Assign Delivery Package")
                        print("4.🔙 Back to main menu")
                        package_choice = input("Enter your choice: ")


                        if package_choice == "1":
                            start_location = input("Enter the start location: ")
                            end_location = input("Enter the end location: ")
                            weight_kg = input("Enter the weight in kilograms: ")
                            contact_information = input("Enter the contact information: ")
                            cmd = cmd_factory.create("createdeliverypackage")
                            result = cmd.execute([start_location, end_location, weight_kg, contact_information])
                            print(result)

                        elif package_choice == "2":
                            package_id_count = input("Enter ID package: ")
                            cmd = cmd_factory.create("viewinformationaboutpackage")
                            result = cmd.execute([package_id_count])
                            print(result)

                        elif package_choice == "3":
                            package_id_count = input("Enter ID package: ")
                            truck_id = input("Enter ID truck: ")
                            cmd = cmd_factory.create("assigndeliverypackage")
                            result = cmd.execute([package_id_count, truck_id])
                            print(result)

                        elif package_choice == "4":
                            continue

                        else:
                            print("Invalid choice. Please try again.")

                    elif choice == "3":
                            print("\nRoute Commands:")
                            print("1. Create Delivery Route")
                            print("2. View Information About Route")
                            print("3. Search for Route")
                            print("4. Back to main menu")
                            route_choice = input("Enter your choice: ")

                            if route_choice == "1":
                                routes = input("Enter route cities: ").split()
                                departure_date = input("Enter departure date (YYYY-MM-DD): ")
                                departure_time = input("Enter departure time (HH:MM): ")
                                cmd = cmd_factory.create("createdeliveryroute")
                                result = cmd.execute(routes + [departure_date, departure_time])
                                print(result)

                            elif route_choice == "2":
                                route_id = input("Enter the route ID: ")
                                cmd = cmd_factory.create("viewinformationaboutroute")
                                result = cmd.execute([route_id])
                                print(result)

                            elif route_choice == "3":
                                start_location = input("Enter the start location: ")
                                end_location = input("Enter the end location: ")
                                cmd = cmd_factory.create("searchforroute")
                                result = cmd.execute([start_location, end_location])
                                print(result)

                            elif route_choice == "4":
                                continue
                            else:
                                print("Invalid choice. Please try again.")

                    elif choice == "4":
                        app_data.logout()
                        print("Logged out successfully!")
                        break

                    elif choice == "5":
                        print("Exiting the application. Goodbye!")
                        break
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
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# 🚪 → Represents logging in/out or exiting.
# 📌 → Highlights the main menu.
# 🚛 → Represents trucks.
# 📦 → Represents package commands.
# 🛤️ → Represents route commands.
# 🔍 → Used for viewing/searching information.
# 🏁 → Assigning a truck (starting a route).
# 📤 → Assigning a package.
# 🔙 → Back to the main menu.
# 🔒 → Logout.
# ❌ → Exit program.
# ⚠️ → Invalid input warning.