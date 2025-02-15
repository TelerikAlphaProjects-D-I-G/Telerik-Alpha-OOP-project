from commands.package_command.assign_delivery_package_command import AssignDeliveryPackageCommand
from commands.truck_command.assign_free_truck_command import AssignFreeTruckCommand
from commands.package_command.create_delivery_package_command import CreateDeliveryPackageCommand
from commands.routes_command.curr_delivery_routes_command import CurrDeliveryRoutesCommand
from commands.package_command.curr_state_delivery_pack_command import CurrStateDeliveryPackCommand
from commands.routes_command.search_for_route_command import SearchForRouteCommand
from commands.routes_command.view_information_rout_command import ViewInformationAboutRouteCommand
from commands.routes_command.create_delivery_route_command import CreateDeliveryRouteCommand
from commands.truck_command.curr_transport_vehicle_command import CurrTransportVehicleCommand
from commands.package_command.view_information_package_command import ViewInformationAboutPackage
from commands.user_command.register_employee_command import RegisterEmployeeCommand
from commands.user_command.login_command import LoginCommand
from commands.user_command.logout_command import LogoutCommand
from commands.user_command.view_logged_in_employee_command import ViewLoggedInEmployeeCommand


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
            return AssignDeliveryPackageCommand(params,self._app_data)
        if cmd.lower() == "assignfreetruck":
            return AssignFreeTruckCommand(self._app_data)
        if cmd.lower() == "currstatedelivpack":
            return CurrStateDeliveryPackCommand(params,self._app_data)
        if cmd.lower() == "currtransportvehicle":
            return CurrTransportVehicleCommand(params,self._app_data)
        if cmd.lower() == "currdeliveryroutes":
            return CurrDeliveryRoutesCommand(params, self._app_data)
        if cmd.lower() == "regiseremployee":
            return RegisterEmployeeCommand(self._app_data)
        if cmd.lower() == "loginemployee":
            return LoginCommand(self._app_data)
        if cmd.lower() == "logoutemployee":
            return LogoutCommand(self._app_data)
        if cmd.lower() == "viewloggedinemployee":
            return ViewLoggedInEmployeeCommand(params, self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')

"""

regiseremployee denkata Denis Denchev Supervisor123 Manager
logoutemployee
loginemployee denkata Supervisor123
searchforroute SYD MEL
createdeliverypackage 1 SYD MEL 45 Pack
viewinformationaboutpackage 1
createdeliveryroute SYD ADL PER ASP 1
assignfreetruck 1001 1
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
regiseremployee gosho Georgi Yovchev 1234568
regiseremployee gosho Georgi Yovchev 1234568 Employee
createdeliverypackage 2 SYD ADL 45 Pack
createdeliveryroute SYD ADL PER DAR 
viewloggedinemployee gosho
viewinformationaboutpackage 2
logoutemployee
end

regiseremployee ivancho Ivan Ivanov manager123 Manager
end
"""
