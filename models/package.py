from models.package_status import PackageStatus
from datetime import datetime, timedelta
from models.route_matrix import Routes



class Package:

	LOCATION_MAPPING = {
		"Sydney": Routes.SYD[0],
		"Melbourne": Routes.MEL[0],
		"Adelaide": Routes.ADL[0],
		"Perth": Routes.PER[0],
		"Brisbane": Routes.BRI[0],
		"Alice Springs": Routes.ASP[0],
		"Darwin": Routes.DAR[0]
	}

	LOCATION_ABBR_MAPPING = {
		Routes.SYD[0]: "Sydney",
		Routes.MEL[0]: "Melbourne",
		Routes.ADL[0]: "Adelaide",
		Routes.PER[0]: "Perth",
		Routes.BRI[0]: "Brisbane",
		Routes.ASP[0]: "Alice Springs",
		Routes.DAR[0]: "Darwin"
	}

	unique_id_user = set()

	def __init__(self, unique_id, start_location, end_location, weight_kg, contact_information):
		if unique_id in Package.unique_id_user:
			raise ValueError("This ID's already exist")
		self._unique_id = unique_id
		self.start_location = self.location_exist(start_location)
		self.end_location = self.location_exist(end_location)
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
		if location in Package.LOCATION_MAPPING:
			return Package.LOCATION_MAPPING[location]
		elif location in Package.LOCATION_ABBR_MAPPING:
			return location
		else:
			raise ValueError('Invalid location!')

	def check_weight(self, value):
		if value < 0:
			raise ValueError('Weight should not be negative')
		self.weight_kg = value

	def revert_status(self):
		self._package_status = PackageStatus.previous(self._package_status)

	def advance_status(self):
		self._package_status = PackageStatus.next(self._package_status)

	def __str__(self):
		start_full_name = Package.LOCATION_ABBR_MAPPING[self.start_location]
		end_full_name = Package.LOCATION_ABBR_MAPPING[self.end_location]

		return (f'Id: {self.unique_id}\n'
				f'Start location: {start_full_name}\n'
				f'End location: {end_full_name}\n'
				f'Weight: {self.weight_kg} kg\n'
				f'Contact information: {self.contact_information}\n'
				f'Current status: {self._package_status}\n'
				f'Estimated delivery time: {str(self.estimated_duration).split(".")[0]} h\n'
				f'Expected delivery date: {self.arrival_time.strftime("%H:%M:%S %d-%m-%Y")}'
				)

new_package = Package('1', 'Sydney', 'Brisbane', 45, 'JohnDue')
new_package.advance_status()
print(new_package)
