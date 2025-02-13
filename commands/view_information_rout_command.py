from commands.base_command import BaseCommand
from commands.validate_params_helpers_command import validate_params_count
from core.application_data import ApplicationData
from models.route_matrix import Routes

class ViewInformationAboutRouteCommand(BaseCommand):

    def __init__(self,params, app_data: ApplicationData):
        super().__init__(app_data)
        self.params = params

    def execute(self):
        super().execute(self.params)
        # test_route = Routes("MEL","SYD","ADL",10)
        # self._app_data.new_route(test_route)
        route_id = super()._try_parse_int(self.params[0])
        route = self._app_data.find_route_by_id(route_id)
        return str(route)

    def _expected_params_count(self) -> int:

        return 1


