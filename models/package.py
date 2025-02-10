from models.package_status import PackageStatus
from datetime import datetime, timedelta


class Package:

	location = {'Sydney', 'Melbourne', 'Adelaide', 'Perth', 'Brisbane', 'Alice Springs', 'Darwin'}

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
		self.location_exist(start_location, end_location)
		self.check_weight(weight_kg)
		self._package_status = PackageStatus.PENDING
		self.created_at = datetime.now
		self.arrival_time = None

	@property
	def package_status(self):
		return self._package_status

	@property
	def unique_id(self):
		return self._unique_id


	def location_exist(self, start_location, end_location):
		if start_location not in Package.location or end_location not in Package.location:
			raise ValueError("Cities must be: 'Sydney', 'Melbourne', 'Adelaide', 'Perth', 'Brisbane', 'Alice Springs', 'Darwin' ")
		if start_location == end_location:
			raise ValueError("Distance must be different")


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
				f'Current status: {self._package_status}'
		        )

new_package = Package('1', 'Adelaide', 'Sydney', 45, 'JohnDue')
new_package.advance_status()
print(new_package)

