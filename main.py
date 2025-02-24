import json
import os
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
                    print("1. Register Employee")
                    print("2. Create Delivery Package")
                    print("3. Create Delivery Route")
                    print("4. View Information About Route")
                    print("5. Search for Route")
                    print("6. Logout")
                    print("7. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        username = input("Enter the username: ")
                        password_employee = input("Enter the password: ")
                        firstname = input("Enter the first name: ")
                        lastname = input("Enter the last name: ")
                        role = input("Enter the role: ")
                        cmd = cmd_factory.create("regiseremployee")
                        result = cmd.execute([username, password_employee, firstname, lastname, role])
                        print(result)

                    elif choice == "2":
                        start_location = input("Enter the start location: ")
                        end_location = input("Enter the end location: ")
                        weight_kg = input("Enter the weight in kilograms: ")
                        contact_information = input("Enter the contact information: ")
                        cmd = cmd_factory.create("createdeliverypackage")
                        result = cmd.execute([start_location, end_location, weight_kg, contact_information])
                        print(result)


                    elif choice == "3":

                        routes = input("Enter route cities: ").split()
                        departure_date = input("Enter departure date (YYYY-MM-DD): ")
                        departure_time = input("Enter departure time (HH:MM): ")
                        cmd = cmd_factory.create("createdeliveryroute")
                        result = cmd.execute(routes + [departure_date, departure_time])
                        print(result)

                    elif choice == "4":
                        route_id = input("Enter the route ID: ")
                        cmd = cmd_factory.create("viewinformationaboutroute")
                        result = cmd.execute([route_id])
                        print(result)

                    elif choice == "5":
                        start_location = input("Enter the start location: ")
                        end_location = input("Enter the end location: ")
                        cmd = cmd_factory.create("searchforroute")
                        result = cmd.execute([start_location, end_location])
                        print(result)
                    elif choice == "6":
                        app_data.logout()
                        print("Logged out successfully!")
                        break
                    elif choice == "7":
                        print("Exiting the application. Goodbye!")

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
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
