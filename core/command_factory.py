from commands.assign_delivery_package_command import AssignDeliveryPackageCommand
from commands.assign_free_truck_command import AssignFreeTruckCommand
from commands.create_delivery_package_command import CreateDeliveryPackageCommand
from commands.curr_delivery_routs_command import CurrDeliveryRoutsCommand
from commands.curr_state_delivery_pack_command import CurrStateDeliveryPackCommand
from commands.search_for_route_command import SearchForRouteCommand
from commands.view_information_rout_command import ViewInformationAboutRouteCommand
from commands.create_delivery_route_command import CreateDeliveryRouteCommand
from commands.curr_transport_vehicle_command import CurrTransportVehicleCommand
from commands.view_information_package_command import ViewInformationAboutPackage
from commands.register_employee_command import RegisterEmployeeCommand
from commands.login_command import LoginCommand
from commands.logout_command import LogoutCommand


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params =input_line.split()

        if cmd.lower() == "createdeliverypackage":
            return CreateDeliveryPackageCommand(params, self._app_data)
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
        if cmd.lower() == "currdeliveryrouts":
            return CurrDeliveryRoutsCommand(params,self._app_data)
        if cmd.lower() == "regiseremployee":
            return RegisterEmployeeCommand(self._app_data)
        if cmd.lower() == "loginemployee":
            return LoginCommand(self._app_data)
        if cmd.lower() == "logoutemployee":
            return LogoutCommand(self._app_data)

        raise ValueError(f'Invalid command name: {cmd}!')
"""
regiseremployee gosho Georgi Yovchev 1234568
logoutemployee
loginemployee gosho 1234568
end


"""

