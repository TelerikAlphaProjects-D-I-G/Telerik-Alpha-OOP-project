import string
from models.route_matrix import Route

from models.employee_role import EmployeeRole


class Employee:

    USERNAME_LEN_MIN = 2
    USERNAME_LEN_MAX = 20
    USERNAME_LEN_ERR = f'Username must be between {USERNAME_LEN_MIN} and {USERNAME_LEN_MAX} characters long!'
    USERNAME_INVALID_SYMBOLS = 'Username contains invalid symbols!'

    PASSWORD_LEN_MIN = 5
    PASSWORD_LEN_MAX = 30
    PASSWORD_LEN_ERR = f'Password must be between {PASSWORD_LEN_MIN} and {PASSWORD_LEN_MAX} characters long!'
    PASSWORD_INVALID_SYMBOLS = 'Password contains invalid symbols!'

    LASTNAME_LEN_MIN = 2
    LASTNAME_LEN_MAX = 20
    LASTNAME_LEN_ERR = f'Lastname must be between {LASTNAME_LEN_MIN} and {LASTNAME_LEN_MAX} characters long!'

    FIRSTNAME_LEN_MIN = 2
    FIRSTNAME_LEN_MAX = 20
    FIRSTNAME_LEN_ERR = f'Firstname must be between {FIRSTNAME_LEN_MIN} and {FIRSTNAME_LEN_MAX} characters long!'


    def __init__(self,username,firstname,lastname,password,employee_role):
        self._username = self.validate_username(username)
        self._firstname = self.validate_first_name(firstname)
        self._lastname = self.validate_last_name(lastname)
        self._password = self.validate_password(password)
        self._employee_role = EmployeeRole.from_string(employee_role)
        self._is_manager = True if employee_role == EmployeeRole.MANAGER else False



    @property
    def username(self):
        return self._username

    @property
    def is_admin(self):
        return self._is_manager

    @property
    def firstname(self):
        return self._firstname

    @property
    def lastname(self):
        return self._lastname

    @property
    def password(self):
        return self._password

    @property
    def employee_role(self):
        return self._employee_role


    @staticmethod
    def validate_username(value):
        forbidden_chars = set("!@#$%^&*()+=[]{}|\\;:'\",<>?/~`")
        if len(value) < Employee.USERNAME_LEN_MIN or len(value) > Employee.USERNAME_LEN_MAX:
            raise ValueError(Employee.USERNAME_LEN_ERR)
        if value.isdigit():
            raise ValueError(Employee.USERNAME_INVALID_SYMBOLS)
        if not value.isalnum:
            raise ValueError(Employee.USERNAME_INVALID_SYMBOLS)
        if any(char in forbidden_chars for char in value):
            raise ValueError(Employee.USERNAME_INVALID_SYMBOLS)

        return value

    @staticmethod
    def validate_first_name(value):
        if Employee.FIRSTNAME_LEN_MIN > len(value) > Employee.FIRSTNAME_LEN_MAX:
            raise ValueError(Employee.FIRSTNAME_LEN_ERR)
        return value

    @staticmethod
    def validate_last_name(value):
        if len(value) < Employee.LASTNAME_LEN_MIN or len(value) > Employee.LASTNAME_LEN_MAX:
            raise ValueError(Employee.LASTNAME_LEN_ERR)
        return value

    @staticmethod
    def validate_password(value):
        if len(value) < Employee.PASSWORD_LEN_MIN or len(value) > Employee.PASSWORD_LEN_MAX:
            raise ValueError(Employee.PASSWORD_LEN_ERR)
        allowed_chars = set(string.ascii_letters + string.digits + "@*-_")
        invalid_char = [char for char in value if char not in allowed_chars]
        if invalid_char:
            raise ValueError(Employee.PASSWORD_INVALID_SYMBOLS)
        return value

    def check_if_manager(self):
        if self._is_manager is False:
            raise ValueError("Your position is not manager")
        return Route.routes_lst

    def check_if_supervisor(self):
        if self.employee_role == EmployeeRole.SUPERVISING_EMPLOYEE:
            pass

    def check_if_employee(self):
        if self.employee_role == EmployeeRole.EMPLOYEE:
            pass

    def __str__(self):
        return (f'Username: {self.username}\n'
                f'Full Name: {self.firstname} {self.lastname}\n'
                f'Role: {self.employee_role}')
