import unittest
from models.employee import Employee
from models.employee_role import EmployeeRole
from models.route_matrix import Route


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("john_doe", "John", "Doe", "Secure@123", "Employee")
        self.manager = Employee("manager01", "Jane", "Smith", "Strong@Pass1", "Manager")

    def test_valid_employee_creation(self):
        self.assertEqual(self.employee.username, "john_doe")
        self.assertEqual(self.employee.firstname, "John")
        self.assertEqual(self.employee.lastname, "Doe")
        self.assertEqual(self.employee.password, "Secure@123")
        self.assertEqual(self.employee.employee_role, EmployeeRole.EMPLOYEE)

    def test_invalid_username_too_short(self):
        with self.assertRaises(ValueError) as cm:
            Employee.validate_username("a")
        self.assertEqual(str(cm.exception), Employee.USERNAME_LEN_ERR)
    #
    def test_invalid_username_symbols(self):
        with self.assertRaises(ValueError) as cm:
            Employee.validate_username("user@123!")
        self.assertEqual(str(cm.exception), Employee.USERNAME_INVALID_SYMBOLS)

    def test_invalid_password_length(self):
        with self.assertRaises(ValueError) as cm:
            Employee.validate_password("a1@")
        self.assertEqual(str(cm.exception), Employee.PASSWORD_LEN_ERR)

    def test_invalid_password_symbols(self):
        with self.assertRaises(ValueError) as cm:
            Employee.validate_password("Password!")
        self.assertEqual(str(cm.exception), Employee.PASSWORD_INVALID_SYMBOLS)

    def test_is_admin_property(self):
        self.assertTrue(self.manager.is_admin)
        self.assertFalse(self.employee.is_admin)

    def test_check_if_manager_valid(self):
        self.assertIsInstance(self.manager.check_if_manager(), list)

    def test_check_if_manager_invalid(self):
        with self.assertRaises(ValueError) as cm:
            self.employee.check_if_manager()
        self.assertEqual(str(cm.exception), "Your position is not manager")

    def test_employee_str(self):
        expected_str = "Username: john_doe\nFull Name: John Doe\nRole: Employee"
        self.assertEqual(str(self.employee), expected_str)

        expected_manager_str = "Username: manager01\nFull Name: Jane Smith\nRole: Manager"
        self.assertEqual(str(self.manager), expected_manager_str)


if __name__ == "__main__":
    unittest.main()

