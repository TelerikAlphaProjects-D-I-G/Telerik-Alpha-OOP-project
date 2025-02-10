from zoneinfo import available_timezones

SCANIA = ["Scania",42000,8000]
MAN = ["Man", 37000, 10000]
ACTROS = ["Actros",  26000,13000]

class Vehicles:

    available_vehicles = {
        'Scania': {'capacity': 42000, 'max range': 8000, 'quantity': 10},
        'Man': {'capacity': 37000, 'max range': 10000, 'quantity': 15},
        'Actros': {'capacity': 26000, 'max range': 13000, 'quantity': 15}
    }

    def __init__(self, name, vehicle_id):
        self.name = name
        self.vehicle_id = vehicle_id
        self.capacity = Vehicles.available_vehicles[name]['capacity']
        self.max_range = Vehicles.available_vehicles[name]['max range']
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
            return Vehicles.available_vehicles.get('Scania')
        if 1011 <= vehicle_id <= 1025:
            return Vehicles.available_vehicles.get('Man')
        if 1026 <= vehicle_id <= 1040:
            return Vehicles.available_vehicles.get('Actros')

    @staticmethod
    def count_vehicles_on_road(lst):
        vehicles_on_road = {'Scania': 0, 'Man': 0, 'Actros': 0}
        for vehicle in lst:
            if not vehicle.is_available:
                vehicles_on_road[vehicle.name] += 1

        available_vehicles_count = {'Scania': Vehicles.available_vehicles['Scania']['quantity'] - vehicles_on_road['Scania'],
                                    'Man': Vehicles.available_vehicles['Man']['quantity'] - vehicles_on_road['Man'],
                                    'Actros': Vehicles.available_vehicles['Actros']['quantity'] - vehicles_on_road['Actros']}

        return vehicles_on_road, available_vehicles_count

    def __str__(self):
        vehicle_info = Vehicles.truck_info(self.vehicle_id)

        if vehicle_info:
            return (f'Name: {self.name}\n'
                    f'Vehicle ID: {self.vehicle_id}\n'
                    f'Capacity: {self.capacity} kg\n'
                    f'Max Range: {self.max_range} km\n'
                    f'Status: {'Available' if self.is_available else 'Not Available'}\n'
                    f'Total Available: {vehicle_info['quantity']} vehicles\n')

        return'No vehicle information has been found.'

scania_vehicle = Vehicles('Scania', 1005)
print(scania_vehicle)

man_vehicle = Vehicles('Man', 1020)
print(man_vehicle)

actros_vehicle = Vehicles('Actros', 1030)
print(actros_vehicle)

scania_vehicle.assign_to_work()
man_vehicle.assign_to_work()
actros_vehicle.assign_to_work()

lst = [scania_vehicle, man_vehicle, actros_vehicle]

vehicles_on_road, available_vehicles = Vehicles.count_vehicles_on_road(lst)



print(f'Vehicles on road: {vehicles_on_road} \nAvailable vehicles: {available_vehicles}')







