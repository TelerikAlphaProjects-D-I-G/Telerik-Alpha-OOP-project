import json
import os

from commands.helper_command.validate_params_helpers_command import try_parse_int
from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from models.package import Package


class Main:
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    print("\n=========================================")
    print("🚛 Welcome to the Logistics Console Application!")
    print("=========================================")

    while True:
        print("\n📌 Please select an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("🔹 Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if app_data.login(username, password):
                print("✅ Login successful!")

                while True:
                    print("\n📌Main Menu:")
                    print(f"Logged in as: {username}\n")
                    print("Please select an option:")
                    print("1.🚛 Truck Commands")
                    print("2.📦 Package Commands")
                    print("3.🛤️ Route Commands")
                    print("4.🔒 Logout")
                    print("5.❌ Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        print("\nTruck Commands:")
                        print("1.🏁 Assign Free Truck to Route")
                        print("2.🔍 View Truck Information")
                        print("3.🚚 Delivered Packages: ")
                        print('4.🚚 Find Trucks in Certain City:')
                        print("5.🔙 Back to main menu")
                        truck_choice = input("Enter your choice: ")

                        if truck_choice == "1":
                            route_id = int(input("Enter ID route: "))
                            truck_id = int(input("Enter ID truck: "))
                            cmd = cmd_factory.create("assignfreetruck")
                            result = cmd.execute([truck_id, route_id])
                            print(result)

                        elif truck_choice == "2":
                            truck_id = int(input("🚛 Enter truck ID: "))
                            cmd = cmd_factory.create("viewinformationabouttruck")
                            result = cmd.execute([truck_id])
                            print(result)

                        elif truck_choice == "3":
                            truck_id = int(input("🚛 Enter Truck ID: "))
                            cmd = cmd_factory.create("startmovement")
                            result = cmd.execute([truck_id])
                            print(result)

                        elif truck_choice == "4":
                            city = input("Enter City: ")
                            cmd = cmd_factory.create("findtrucksincity")
                            result = cmd.execute([city])
                            print(result)

                        elif choice == "5":
                            continue

                        else:
                            print('Invalid choice. Please try again.')



                    elif choice == "2":
                        print("\n📦 Package Commands:")
                        print("1.📦 Create Delivery Package")
                        print("2.🔍 View Information About Package")
                        print("3.🚛 Assign Delivery Package to Truck")
                        print("4.🔍 View Information About Unassigned Packages ")
                        print("5.🔙 Back to Main Menu")
                        package_choice = input("➡️Enter your choice: ")


                        if package_choice == "1":
                            print("\n📦 Creating a new package...")
                            start_location = input("📍 Enter start location: ")
                            end_location = input("🏁 Enter end location: ")
                            weight_kg = input("⚖️ Enter the weight in kilograms: ")
                            contact_information = input("📞 Enter the contact information: ")
                            cmd = cmd_factory.create("createdeliverypackage")
                            result = cmd.execute([start_location, end_location, weight_kg, contact_information])
                            print(result)

                        elif package_choice == "2":
                            package_id_count = input("🔍 Enter ID of the package: ")
                            cmd = cmd_factory.create("viewinformationaboutpackage")
                            result = cmd.execute([package_id_count])
                            print(result)

                        elif package_choice == "3":
                            print("\n🚛 Assigning Package to Truck...")
                            package_id_count = input("📦 Enter ID of the package: ")
                            truck_id = input("🚛 Enter ID of the truck: ")
                            cmd = cmd_factory.create("assigndeliverypackage")
                            result = cmd.execute([package_id_count, truck_id])
                            print(result)

                        elif package_choice == "4":
                            cmd = cmd_factory.create("allpendingpackageview")
                            result = cmd.execute()
                            print(result)

                        elif package_choice == "5":
                            continue

                        else:
                            print("❌Invalid choice. Please try again.")

                    elif choice == "3":
                            print("\n🛣️ Route Commands:")
                            print("1.🛤️ Create Delivery Route")
                            print("2.🗺️ View Information About Route")
                            print("3.🔍 Search for Route")
                            print("4.🔍 View all Routes")
                            print("5.🔙 Back to Main Menu")
                            route_choice = input("➡️Enter your choice: ")

                            if route_choice == "1":
                                print("\n🛤️ Creating a new delivery route...")
                                routes = input("📍 Enter route cities (separated by space): ").split()
                                departure_date = input("📅 Enter departure date (YYYY-MM-DD): ")
                                departure_time = input("⏰ Enter departure time (HH:MM): ")
                                cmd = cmd_factory.create("createdeliveryroute")
                                result = cmd.execute(routes + [departure_date, departure_time])
                                print(result)

                            elif route_choice == "2":
                                route_id = input("🗺️ Enter the route ID: ")
                                cmd = cmd_factory.create("viewinformationaboutroute")
                                result = cmd.execute([route_id])
                                print(result)

                            elif route_choice == "3":
                                print("\n🔍 Searching for a route...")
                                start_location = input("📍 Enter the start location: ")
                                end_location = input("🏁 Enter the destination: ")
                                cmd = cmd_factory.create("searchforroute")
                                result = cmd.execute([start_location, end_location])
                                print(result)

                            elif route_choice == "4":
                                cmd = cmd_factory.create("printroutes")
                                result = cmd.execute()
                                print(result)


                            elif route_choice == "5":
                                continue
                            else:
                                print("❌Invalid choice. Please try again.")

                    elif choice == "4":
                        app_data.logout()
                        print("✅ Logged out successfully!")
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
                print("✅ User created successfully!")
            else:
                print("Failed to create user. Username may already exist.")

        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


