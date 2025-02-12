
SCANIA = ["Scania",42000,8000]
MAN = ["Man", 37000, 10000]
ACTROS = ["Actros",  26000,13000]

class Vehicle:

    available_vehicles = {
        'Scania': {'capacity': 42000, 'max range': 8000, 'quantity': 10},
        'Man': {'capacity': 37000, 'max range': 10000, 'quantity': 15},
        'Actros': {'capacity': 26000, 'max range': 13000, 'quantity': 15}
    }

    def __init__(self, name, vehicle_id,max_range,capacity):
        self.name = name
        self.vehicle_id = vehicle_id
        self.capacity = Vehicle.available_vehicles[name]['capacity']
        self.max_range = Vehicle.available_vehicles[name]['max range']
        self.is_available = True
        self._vehicles = []

    @property
    def vehicles(self):
        return self._vehicles

    def assign_to_work(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def work_done(self):
        self.is_available = True
        return True


    def truck_info(self,vehicle_id):
        for truck_id in range(1001,1011):
            vehicle = Vehicle("Scania",truck_id,8000,42000)
            self.vehicles.append(vehicle)
        for truck_id in range(1011,1025):
            vehicle = Vehicle("Man", truck_id,10000,37000)
            self.vehicles.append(vehicle)
        for truck_id in range(1026,1040):
            vehicle = Vehicle("Actros",truck_id,13000,26000)
            self.vehicles.append(vehicle)

    @staticmethod
    def count_vehicles_on_road(lst):
        vehicles_on_road = {'Scania': 0, 'Man': 0, 'Actros': 0}
        for vehicle in lst:
            if not vehicle.is_available:
                vehicles_on_road[vehicle.name] += 1

        liable_vehicles_count = {'Scania': Vehicle.available_vehicles['Scania']['quantity'] - vehicles_on_road['Scania'],
                                    'Man': Vehicle.available_vehicles['Man']['quantity'] - vehicles_on_road['Man'],
                                    'Actros': Vehicle.available_vehicles['Actros']['quantity'] - vehicles_on_road['Actros']}

        return vehicles_on_road, liable_vehicles_count

    def __str__(self):
        vehicle_info = self.truck_info(self.vehicle_id)

        if vehicle_info:
            return (f'Name: {self.name}\n'
                    f'Vehicle ID: {self.vehicle_id}\n'
                    f'Capacity: {self.capacity} kg\n'
                    f'Max Range: {self.max_range} km\n'
                    f'Status: {'Available' if self.is_available else 'Not Available'}\n'
                    f'Total Available: {vehicle_info['quantity']} vehicles\n')

        return'No vehicle information has been found.'

scania_vehicle = Vehicle('Scania', 1005,8000,42000)
print(scania_vehicle)

man_vehicle = Vehicle('Man', 1020,10000,37000)
print(man_vehicle)

actros_vehicle = Vehicle('Actros', 1030,13000,26000)
print(actros_vehicle)

scania_vehicle.assign_to_work()
man_vehicle.assign_to_work()
actros_vehicle.assign_to_work()
#
lst = [scania_vehicle, man_vehicle, actros_vehicle]
#
vehicles_on_road, available_vehicles_count = Vehicle.count_vehicles_on_road(lst)

scania_on_road, man_on_road, actros_on_road = vehicles_on_road.values()
scania_available, man_available, actros_available = available_vehicles_count.values()
print()
print(f"Vehicles on the road:")
print(f"Scania: {scania_on_road}, Man: {man_on_road}, Actros: {actros_on_road}")
print("\nAvailable vehicles:")
print(f"Scania: {scania_available}, Man: {man_available}, Actros: {actros_available}")