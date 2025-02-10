SCANIA = ["Scania",42000,8000]
MAN = ["Man", 37000, 10000]
ACTROS = ["Actros",  26000,13000]

class Vehicles:

    def __init__(self, name, capacity, max_range, vehicle_id):
        self.name = name
        self.capacity = capacity
        self.max_range = max_range
        self.vehicle_id = vehicle_id
        self.is_available = True

    def assign_to_work(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def work_done(self):
        self.is_available = True
        return True

    @staticmethod
    def truck_info(vehicle_id):
        if 1001 <= vehicle_id <= 1010:
            return SCANIA
        if 1011 <= vehicle_id <= 1025:
            return MAN
        if 1026 <= vehicle_id <= 1040:
            return ACTROS

    def __str__(self):
        return f"\n{self.name}, \n{self.truck_info}"

print(*Vehicles.truck_info(1024))





