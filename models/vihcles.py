
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





