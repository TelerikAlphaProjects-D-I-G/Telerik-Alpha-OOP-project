from commands.helper_command.base_command import BaseCommand
from core.application_data import ApplicationData


class LogoutCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._app_data.logout()

        return '\nYou logged out!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 0
