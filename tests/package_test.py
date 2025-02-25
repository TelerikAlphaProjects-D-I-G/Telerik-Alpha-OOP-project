import unittest
from models.package import Package
from models.package_status import PackageStatus
from models.route_matrix import Route
from models.vehicles import Vehicles


class TestPackage(unittest.TestCase):
    def setUp(self):
        self.package = Package("Sydney", "Melbourne", 10, "John Doe")
        self.truck = Vehicles(1001)

    def test_package_initialization(self):
        self.assertEqual(self.package.start_location, Route.SYD[0])
        self.assertEqual(self.package.end_location, Route.MEL[0])
        self.assertEqual(self.package.weight_kg, 10)
        self.assertEqual(self.package.contact_information, "John Doe")
        self.assertEqual(self.package.package_status, PackageStatus.PENDING)

    def test_package_weight_validation(self):
        with self.assertRaises(ValueError):
            Package("Sydney", "Melbourne", -5, "Invalid Weight")

    def test_package_invalid_location(self):
        with self.assertRaises(ValueError):
            Package("InvalidCity", "Melbourne", 10, "John Doe")

    def test_package_assign_to_truck(self):
        self.package.assign_to_truck(self.truck)
        self.assertEqual(self.package.assigned_truck, self.truck)
        self.assertIn(self.package, self.truck.assigned_packages)
        self.assertEqual(self.truck.current_load, 10)

    def test_package_status_transitions(self):
        self.package.advance_status()
        self.assertEqual(self.package.package_status, PackageStatus.next(PackageStatus.PENDING))

        self.package.revert_status()
        self.assertEqual(self.package.package_status, PackageStatus.PENDING)


    def test_string_representation(self):
        expected_str = (f'\n📦 PACKAGE DETAILS\n'
                        f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
                        f'🆔 ID                 : 9\n'
                        f'📍 Start Location     : Sydney\n'
                        f'📍 End Location       : Melbourne\n'
                        f'📦⚖️ Weight           : 10 kg\n'
                        f'📋 Contact Info       : John Doe\n'
                        f'✅ Current Status     : Pending\n'
                        f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        self.assertEqual(str(self.package), expected_str)

if __name__ == "__main__":
    unittest.main()