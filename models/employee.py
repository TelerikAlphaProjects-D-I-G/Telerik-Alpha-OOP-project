import string

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

    NORMAL_ROLE_VEHICLE_LIMIT = 5

    NORMAL_USER_LIMIT_REACHED_ERR = f'You are not VIP and cannot add more than {NORMAL_ROLE_VEHICLE_LIMIT} vehicles!'
    ADMIN_CANNOT_ADD_VEHICLES_ERR = 'You are an admin and therefore cannot add vehicles!'
    YOU_ARE_NOT_THE_AUTHOR = 'You are not the author of the comment you are trying to remove!'
    THE_VEHICLE_DOES_NOT_EXIT = 'The vehicle does not exist!'

    def __init__(self,username,firstname,lastname,password,user_role):
        self._username = self.validate_username(username)
        self._firstname = self.validate_first_name(firstname)
        self._lastname = self.validate_last_name(lastname)
        self._password = self.validate_password(password)
        self._user_role = user_role
        self._is_manager = True if user_role == EmployeeRole.MANAGER else False
        self._vehicles = []


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
    def user_role(self):
        return self._user_role


    @staticmethod
    def validate_username(value):
        if len(value) < Employee.USERNAME_LEN_MIN or len(value) > Employee.USERNAME_LEN_MAX:
            raise ValueError(Employee.USERNAME_LEN_ERR)
        if not value.isalnum():
            raise ValueError(Employee.USERNAME_INVALID_SYMBOLS)
        return value

    @staticmethod
    def validate_first_name(value):
        if len(value) < Employee.FIRSTNAME_LEN_MIN or len(value) > Employee.FIRSTNAME_LEN_MAX:
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


    def __str__(self):
        return f'Username: {self.username}, FullName: {self.firstname} {self.lastname}, Role: {self.user_role}'
