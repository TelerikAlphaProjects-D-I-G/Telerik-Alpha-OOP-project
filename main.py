from core.application_data import ApplicationData
from core.command_factory import CommandFactory

def main():
    app_data = ApplicationData()
    cmd_factory = CommandFactory(app_data)

    # Login


    print("Welcome to the Logistics Console Application!")

    while True:
        print("\nPlease select an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            try:
                employee = app_data.find_employee_by_username(username)
                if employee and employee.password == password:
                    app_data.login(employee)
                    print("Login successful!")

                    while True:
                        print("\nLogged in as:", employee.username)
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
                            # Register Employee
                            cmd_factory.create("regiseremployee").execute()
                        elif choice == "2":
                             start_location = input("Enter the start location: ")
                             end_location = input("Enter the end location: ")
                             weight_kg = input("Enter the weight in kilograms: ")
                             contact_information = input("Enter the contact information: ")
                            # Create Delivery Package
                             cmd_factory.create("createdeliverypackage").execute([start_location, end_location, weight_kg, contact_information])
                        elif choice == "3":
                            # Create Delivery Route
                            cmd_factory.create("createdeliveryroute").execute()
                        elif choice == "4":
                            # View Information About Route
                            cmd_factory.create("viewinformationaboutroute").execute()
                        elif choice == "5":
                            # Search for Route
                            cmd_factory.create("searchforroute").execute()
                        elif choice == "6":
                            # Logout
                            app_data.logout()
                            print("Logged out successfully!")
                            break
                        elif choice == "7":
                            # Exit
                            print("Exiting the application. Goodbye!")
                            return
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Invalid password. Please try again.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            # Register
            username = input("Enter your desired username: ")
            password = input("Enter your desired password: ")
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            position = input("Enter your position: ")

            cmd_factory.create("regiseremployee").execute([username, password, first_name, last_name, position])
            print("User created successfully!")
        elif choice == "3":
            # Exit
            print("Exiting the application. Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()