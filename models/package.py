from numpy.f2py.cfuncs import needs


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


	def __str__(self):

		return (f'Id: {self.unique_id}\n'
		        f'Start location: {self.start_location}\n'
		        f'End location: {self.end_location}\n'
		        f'Weight: {self.weight_kg} kg\n'
		        f'Contact information: {self.contact_information}\n'
		        )
new_package = Package('1', 'Adelaide', 'Sydney', 45, 'JohnDue')
print(new_package)


