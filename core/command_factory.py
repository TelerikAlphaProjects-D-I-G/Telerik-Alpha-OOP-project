from commands.assign_delivery_package_command import AssignDeliveryPackageCommand
from commands.assign_free_truck_command import AssignFreeTruckCommand
from commands.create_delivery_package_command import CreateDeliveryPackageCommand
from commands.curr_delivery_routes_command import CurrDeliveryRoutesCommand
from commands.curr_state_delivery_pack_command import CurrStateDeliveryPackCommand
from commands.search_for_route_command import SearchForRouteCommand
from commands.view_information_rout_command import ViewInformationAboutRouteCommand
from commands.create_delivery_route_command import CreateDeliveryRouteCommand
from commands.curr_transport_vehicle_command import CurrTransportVehicleCommand
from commands.view_information_package_command import ViewInformationAboutPackage
from commands.register_employee_command import RegisterEmployeeCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand
from commands.view_logged_in_employee_command import ViewLoggedInEmployeeCommand


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
            return AssignFreeTruckCommand(params,self._app_data)
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

regiseremployee denkata Denis Denchev Supervisor123 Employee
logoutemployee
loginemployee denkata Supervisor123
searchforroute SYD MEL
createdeliverypackage 1 SYD MEL 45 Pack
viewinformationaboutpackage 1
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
