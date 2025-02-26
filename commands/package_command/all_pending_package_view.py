from models.employee_role import EmployeeRole
from models.package_status import PackageStatus


class AllPendingPackageView:
    def __init__(self, app_data):
        self.app_data = app_data

    def execute(self):

        employee = self.app_data.logged_in_employee
        if employee.employee_role not in [EmployeeRole.SUPERVISING_EMPLOYEE, EmployeeRole.MANAGER]:
            return '\nError: Only Supervisors and Managers have access to this data!'

        pending_packages = self.app_data.get_packages_by_status()
        if not pending_packages:
            return "\n📦 Not delivery package pending."
        for package in pending_packages:
                print(f"\n📦 Package ID: {package.package_id_count}")
                print(f"⚖️ Weight: {package.weight_kg}")
                print(f"📍 Start Location: {package.start_location}")
                print(f"🏁 End Location: {package.end_location}")
                print(f"📦 Package Status: {package.package_status}")
                print(f"📞 Contact information: {package.contact_information}")
                print("------------------------")
        return "✅ Packages displayed successfully!"
    def _requires_login(self) -> bool:
        return False