import unittest
from datetime import datetime, timedelta
from models.route_matrix import Route
from models.vehicles import Vehicles


class TestRoute(unittest.TestCase):
    def setUp(self):
        self.route1 = Route("SYD", "MEL", departure_time=datetime(2025, 3, 1, 8, 0, 0))
        self.route2 = Route("ADL", "BRI", ["MEL", "SYD"], departure_time=datetime(2025, 3, 2, 9, 30, 0))
        self.vehicle1 = Vehicles(1011)
        self.vehicle2 = Vehicles(1002)

    def test_route_creation(self):
        self.assertEqual(self.route1.start_location, "SYD")
        self.assertEqual(self.route1.end_location, "MEL")
        self.assertEqual(self.route1.additional_stops, None)
        self.assertEqual(self.route2.start_location, "ADL")
        self.assertEqual(self.route2.end_location, "BRI")
        self.assertEqual(self.route2.additional_stops, ["MEL", "SYD"])


    def test_assign_vehicle_success(self):
        result = self.route1.assign_vehicle(1011)
        self.assertTrue(result)
        self.assertIsInstance(self.route1.assigned_vehicle, Vehicles)
        self.assertEqual(self.route1.assigned_vehicle.vehicle_id, 1011)

    def test_assign_vehicle_fail_already_assigned(self):
        self.route1.assign_vehicle(1011)
        result = self.route1.assign_vehicle(1002)
        self.assertFalse(result)

    def test_calculate_total_distance_valid(self):
        total_distance, stop_distances = Route.calculate_total_distance(["SYD", "MEL", "ADL"])
        self.assertEqual(total_distance, 877 + 725)
        self.assertIn("SYD → MEL: 877 km", stop_distances)
        self.assertIn("MEL → ADL: 725 km", stop_distances)

    def test_calculate_total_distance_invalid(self):
        with self.assertRaises(ValueError):
            Route.calculate_total_distance(["SYD", "XYZ"])

    def test_get_arrival_times(self):
        arrival_times = self.route2.get_arrival_times()
        self.assertIsInstance(arrival_times, list)
        self.assertGreater(len(arrival_times), 0)
        self.assertEqual(arrival_times[0][0], "MEL")
        self.assertEqual(arrival_times[-1][0], "BRI")

    def test_str_method(self):
        self.route1.assign_vehicle(1011)
        expected_str = (
            f"Route id: {self.route1.route_id}\n"
            "Start location: SYD\n"
            "End location: MEL\n"
            "Assigned vehicle: 1011"
        )
        self.assertEqual(str(self.route1), expected_str)


if __name__ == "__main__":
    unittest.main()
