from models.package_status import PackageStatus
from datetime import datetime, timedelta
from models.route_matrix import Routes

from models.route_matrix import Routes


class Package:
	LOCATION_MAPPING = {
		"Sydney": "SYD",
		"Melbourne": "MEL",
		"Adelaide": "ADL",
		"Perth": "PER",
		"Brisbane": "BRI",
		"Alice Springs": "ASP",
		"Darwin": "DAR"
	}

	unique_id_user = set()

	def __init__(self, unique_id, start_location, end_location, weight_kg, contact_information):
		if unique_id in Package.unique_id_user:
			raise ValueError("This ID's already exist")
		self._unique_id = unique_id
		self.start_location = start_location
		self.end_location = end_location
		self.weight_kg = weight_kg
		self.contact_information = contact_information
		Package.unique_id_user.add(unique_id)
#		self.location_exist(start_location, end_location)
		self.check_weight(weight_kg)
		self._package_status = PackageStatus.PENDING
		self.estimated_duration = Routes.time_needed(self.start_location, self.end_location)
		self.arrival_time = datetime.now() + self.estimated_duration if self.estimated_duration else None

	@property
	def package_status(self):
		return self._package_status

	@property
	def unique_id(self):
		return self._unique_id


	def location_exist(self, location):
		if location in Package.LOCATIONS_FULL:
			return Package.LOCATION_MAPPING[location]
		elif location in Package.LOCATIONS_ABBR:
			return location
		else:
			raise ValueError(f"Invalid location: {location}. Must be one of: {', '.join(Package.LOCATIONS_FULL)}")


	def check_weight(self, value):
		if value < 0:
			raise ValueError('Weight should not be negative')
		self.weight_kg = value

	def revert_status(self):
		self._package_status = PackageStatus.previous(self._package_status)

	def advance_status(self):
		self._package_status = PackageStatus.next(self._package_status)


	def __str__(self):

		return (f'Id: {self.unique_id}\n'
		        f'Start location: {self.start_location}\n'
		        f'End location: {self.end_location}\n'
		        f'Weight: {self.weight_kg} kg\n'
		        f'Contact information: {self.contact_information}\n'
				f'Current status: {self._package_status}\n'
				f'Estimated delivery time: {str(self.estimated_duration).split(".")[0]}\n'
				f'Expected delivery date: {self.arrival_time.strftime("%Y-%m-%d %H:%M:%S")}'
				)

new_package = Package('1', 'SYD', 'MEL', 45, 'JohnDue')
new_package.advance_status()
print(new_package)

