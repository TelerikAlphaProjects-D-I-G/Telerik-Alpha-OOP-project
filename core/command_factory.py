from commands.package_command.all_pending_package_view import AllPendingPackageView
from commands.package_command.assign_delivery_package_command import AssignDeliveryPackageCommand
from commands.truck_command.assign_free_truck_command import AssignFreeTruckCommand
from commands.package_command.create_delivery_package_command import CreateDeliveryPackageCommand
from commands.routes_command.search_for_route_command import SearchForRouteCommand
from commands.routes_command.view_information_route_command import ViewInformationAboutRouteCommand
from commands.routes_command.create_delivery_route_command import CreateDeliveryRouteCommand
from commands.package_command.view_information_package_command import ViewInformationAboutPackage
from commands.user_command.register_employee_command import RegisterEmployeeCommand
from commands.user_command.login_command import LoginCommand
from commands.user_command.logout_command import LogoutCommand
from commands.user_command.view_logged_in_employee_command import ViewLoggedInEmployeeCommand
from commands.routes_command.print_routes import PrintRoutes
from commands.truck_command.view_information_truck_command import ViewInformationAboutTruck
from commands.truck_command.find_trucks_in_city_command import FindTrucksInCityCommand
from commands.truck_command.start_movement_truck_command import StartMovementTruckCommand

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params =input_line.split()

        if cmd.lower() == "createdeliverypackage":
            return CreateDeliveryPackageCommand(self._app_data)
        if cmd.lower() == "createdeliveryroute":
            return CreateDeliveryRouteCommand(params, self._app_data)
        if cmd.lower() == "searchforroute":
            return SearchForRouteCommand(params,self._app_data)
        if cmd.lower() == "viewinformationaboutroute":
            return ViewInformationAboutRouteCommand(params,self._app_data)
        if cmd.lower() == "viewinformationaboutpackage":
            return ViewInformationAboutPackage(params, self._app_data)
        if cmd.lower() == "assigndeliverypackage":
            return AssignDeliveryPackageCommand(self._app_data)
        if cmd.lower() == "startmovement":
            return StartMovementTruckCommand(self._app_data)
        if cmd.lower() == "assignfreetruck":
            return AssignFreeTruckCommand(self._app_data)
        if cmd.lower() == "regiseremployee":
            return RegisterEmployeeCommand(self._app_data)
        if cmd.lower() == "loginemployee":
            return LoginCommand(self._app_data)
        if cmd.lower() == "logoutemployee":
            return LogoutCommand(self._app_data)
        if cmd.lower() == "viewloggedinemployee":
            return ViewLoggedInEmployeeCommand(params, self._app_data)
        if cmd.lower() == "printroutes":
            return PrintRoutes(self._app_data)
        if cmd.lower() == "viewinformationabouttruck":
            return ViewInformationAboutTruck(params, self._app_data)
        if cmd.lower() == 'findtrucksincity':
            return FindTrucksInCityCommand(params, self._app_data)
        if cmd.lower() == 'allpendingpackageview':
            return AllPendingPackageView(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')

"""

regiseremployee denkata Denis Denchev Supervisor123 Manager
searchforroute SYD MEL
logoutemployee
loginemployee denkata Supervisor123
searchforroute SYD MEL ADL
createdeliverypackage 1 SYD MEL 45 Pack
assigndeliverypackage
viewinformationaboutpackage 1
createdeliveryroute SYD MEL PER
assignfreetruck 1001 1
assigndeliverypackage 1 1009 1
end

regiseremployee denkata Denis Denchev Supervisor123 Manager
logoutemployee
loginemployee denkata Supervisor123
createdeliveryroute SYD ADL MEL
assignfreetruck 1001 1
end


viewloggedinemployee denkata
logoutemployee
regiseremployee ivancho Ivan Pustovit manager123 Manager
createdeliverypackage 1 SYD MEL 45 Pack
viewinformationaboutpackage 1
viewloggedinemployee ivancho
logoutemployee
viewinformationaboutpackage 1
regiseremployee gosho Georgi Yovchev 1234568 Employee
regiseremployee gosho Georgi Yovchev 1234568 Employee
createdeliverypackage 2 SYD ADL 45 Pack
createdeliveryroute SYD ADL PER DAR 
viewloggedinemployee gosho
viewinformationaboutpackage 2
logoutemployee
end

regiseremployee ivancho Ivan Ivanov manager123 Manager
createdeliverypackage 1 SYD MEL 45 Ivan
end

regiseremployee ivancho Ivan Pustovit manager123 Manager
createdeliverypackage 1 SYD MEL 45 Ivan
createdeliveryroute SYD MEL PER ADL 2025-02-22 11:30
assignfreetruck 1002 1
assigndeliverypackage 1 1001 
viewinformationaboutpackage 1
viewinformationaboutroute 1
end

regiseremployee ivancho Ivan Pustovit manager123 Manager
createdeliverypackage Sydney Melbourne 45 Ivan
createdeliveryroute SYD MEL PER
createdeliveryroute BRI SYD MEL ADL 2025-02-22 11:30
createdeliveryroute DAR ASP SYD 2025-02-22 12:30
createdeliveryroute DAR ASP ADL 2025-02-22 08:30
createdeliveryroute MEL SYD BRI 2025-02-23 12:30
createdeliveryroute SYD MEL 2025-02-22 14:30
viewinformationaboutroute 1
searchforroute SYD MEL
end

printroutes

regiseremployee ivancho Ivan Pustovit manager123 Manager
createdeliverypackage 1 SYD MEL 45 Ivan
createdeliveryroute BRI SYD MEL ADL 2025-02-22 11:30
assignfreetruck 1001 1
assigndeliverypackage 1 1001
viewinformationaboutpackage 1
viewinformationaboutroute 1
viewinformationabouttruck 1001 1
end
regiseremployee ivancho Ivan Pustovit manager123 Manager
viewinformationabouttruck 1001
end

regiseremployee ivancho Ivan Pustovit manager123 Manager
createdeliveryroute BRI SYD MEL ADL 2025-02-22 11:30
createdeliverypackage 1 SYD MEL 45 Ivan
searchforroute SYD MEL
end
assignfreetruck 1001 1
viewinformationaboutroute 1
assigndeliverypackage 1 1001
viewinformationaboutpackage 1
end

"""

