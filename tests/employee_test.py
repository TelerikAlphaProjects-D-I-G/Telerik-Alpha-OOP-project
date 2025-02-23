import unittest
from models.employee import Employee
from models.employee_role import EmployeeRole
from models.route_matrix import Route


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("john_doe", True, "John", "Doe", "Secure@123")
        self.manager = Employee("manager01", True, "Jane", "Smith", "Strong@Pass1")

    def test_username_property(self):
        self.assertEqual(self.employee.username, "john_doe")

    def test_is_admin_property(self):
        self.assertTrue(self.employee.is_admin)

    def test_firstname_property(self):
        self.assertEqual(self.employee.firstname, "John")

    def test_lastname_property(self):
        self.assertEqual(self.employee.lastname, "Doe")

    def test_password_property(self):
        self.assertEqual(self.employee.password, "Secure@123")

    def test_employee_role_property(self):
        self.assertEqual(self.employee.employee_role, EmployeeRole.EMPLOYEE)

    def test_validate_username_valid(self):
        self.assertEqual(Employee.validate_username("ValidUser123"), "ValidUser123")

    def test_validate_username_too_short(self):
        with self.assertRaises(ValueError):
            Employee.validate_username("ab")

    def test_validate_username_too_long(self):
        with self.assertRaises(ValueError):
            Employee.validate_username("a" * (Employee.USERNAME_LEN_MAX + 1))

    def test_validate_username_invalid_symbols(self):
        with self.assertRaises(ValueError):
            Employee.validate_username("Invalid@User!")

    def test_validate_firstname_valid(self):
        self.assertEqual(Employee.validate_first_name("John"), "John")

    def test_validate_firstname_too_short(self):
        with self.assertRaises(ValueError):
            Employee.validate_first_name("J")

    def test_validate_lastname_valid(self):
        self.assertEqual(Employee.validate_last_name("Doe"), "Doe")

    def test_validate_lastname_too_long(self):
        with self.assertRaises(ValueError):
            Employee.validate_last_name("D" * (Employee.LASTNAME_LEN_MAX + 1))

    def test_validate_password_valid(self):
        self.assertEqual(Employee.validate_password("Strong@123"), "Strong@123")

    def test_validate_password_invalid_symbols(self):
        with self.assertRaises(ValueError):
            Employee.validate_password("InvalidPassword!")

    def test_check_if_manager_valid(self):
        self.assertEqual(self.manager.check_if_manager(), Route.routes_lst)

    def test_check_if_manager_invalid(self):
        with self.assertRaises(ValueError):
            self.employee.check_if_manager()

    def test_employee_str(self):
        expected_str = "Username: john_doe\nFull Name: John Doe\nRole: Employee"
        self.assertEqual(str(self.employee), expected_str)


if __name__ == "__main__":
    unittest.main()
