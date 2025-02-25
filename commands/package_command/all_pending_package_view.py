from models.employee_role import EmployeeRole
from models.package_status import PackageStatus


class AllPendingPackageView:
    def __init__(self, app_data):
        self.app_data = app_data


    def execute(self):
        pending_packages = self.app_data.get_packages_by_status()
        pending_packages = self.app_data.get_packages_by_status()

        for package in pending_packages:
            return  (f"\nPackage ID: {package.package_id_count}"
                f"Weight: {package.weight_kg}\n"
                f"Start Location: {package.start_location}\n"
                f"End Location: {package.end_location}\n"
                f"Package Status: {package.package_status}\n"
                "------------------------"
                 )









    def _requires_login(self) -> bool:
        return False