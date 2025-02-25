import unittest
from models.vehicles import Vehicles

TRUCKS = {
    1022: {"model": "Actros", "capacity": 26000, "max_range": 13000, "city": "SYD"},
    1002: {"model": "Scania", "capacity": 42000, "max_range": 8000, "city": "ADL"},
    1011: {"model": "Man", "capacity": 37000, "max_range": 10000, "city": "SYD"},
}


class TestVehicles(unittest.TestCase):
    def setUp(self):
        self.truck1 = Vehicles(1011)
        self.truck2 = Vehicles(1002)
        self.unknown_truck = Vehicles(10111)

    def test_vehicle_creation_valid(self):
        self.assertEqual(self.truck1.name, "Man")
        self.assertEqual(self.truck1.capacity, 37000)
        self.assertEqual(self.truck1.max_range, 10000)
        self.assertEqual(self.truck1.current_city, "ADL")

    def test_vehicle_creation_unknown(self):
        self.assertEqual(self.unknown_truck.name, "uknown model")
        self.assertEqual(self.unknown_truck.capacity, 0)
        self.assertEqual(self.unknown_truck.max_range, 0)
        self.assertEqual(self.unknown_truck.current_city, "uknown city")

    def test_assign_vehicle_success(self):
        result = self.truck1.assign_vehicle(1011)
        self.assertTrue(result)
        self.assertEqual(self.truck1.assigned_vehicle, 1011)

    def test_assign_vehicle_fail_already_assigned(self):
        self.truck1.assign_vehicle(1011)
        result = self.truck1.assign_vehicle(1011)
        self.assertFalse(result)

    def test_assign_to_work_success(self):
        result = self.truck1.assign_to_work()
        self.assertTrue(result)
        self.assertFalse(self.truck1.is_available)

    def test_assign_to_work_fail_already_busy(self):
        self.truck1.assign_to_work()
        result = self.truck1.assign_to_work()
        self.assertFalse(result)

    def test_work_done(self):
        self.truck1.assign_to_work()
        self.truck1.work_done()
        self.assertTrue(self.truck1.is_available)
        self.assertEqual(self.truck1.current_load, 0)
        self.assertEqual(len(self.truck1.assigned_packages), 0)

    def test_str_method(self):
        expected_str = (
            "Name: Man\n"
            "Vehicle ID: 1011\n"
            "Capacity: 37000 kg\n"
            "Max Range: 10000 km\n"
            'Status: Available\n'
            'Current Load: 0 kg\n'
            'Assigned Packages: None\n'
            'Current city: ADL'
        )
        self.assertEqual(str(self.truck1), expected_str)


if __name__ == "__main__":
    unittest.main()
