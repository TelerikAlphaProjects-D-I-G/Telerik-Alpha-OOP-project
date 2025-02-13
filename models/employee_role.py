class EmployeeRole:
    EMPLOYEE = 'Employee'
    SUPERVISING_EMPLOYEE = 'Supervisor'
    MANAGER = "Manager"

    @classmethod
    def from_string(cls, value) -> str:
        if value not in [cls.EMPLOYEE, cls.SUPERVISING_EMPLOYEE, cls.MANAGER]:
            raise ValueError(
                f'None of the possible EmployeeRole values matches the value {value}.')

        return value
