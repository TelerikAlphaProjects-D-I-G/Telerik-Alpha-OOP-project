from commands.helper_command.validate_params_helpers_command import try_parse_int
from models.package_status import PackageStatus
from datetime import datetime, timedelta
from models.route_matrix import Route
from models.vehicles import Vehicles


class Package:



	LOCATION_MAPPING = {
		"Sydney": Route.SYD[0],
		"Melbourne": Route.MEL[0],
		"Adelaide": Route.ADL[0],
		"Perth": Route.PER[0],
		"Brisbane": Route.BRI[0],
		"Alice Springs": Route.ASP[0],
		"Darwin": Route.DAR[0]
	}

	LOCATION_ABBR_MAPPING = {
		Route.SYD[0]: "Sydney",
		Route.MEL[0]: "Melbourne",
		Route.ADL[0]: "Adelaide",
		Route.PER[0]: "Perth",
		Route.BRI[0]: "Brisbane",
		Route.ASP[0]: "Alice Springs",
		Route.DAR[0]: "Darwin"
	}

	package_id_counter = 0

	def __init__(self,  start_location, end_location, weight_kg, contact_information):
		Package.package_id_counter += 1
		self.package_id_count = Package.package_id_counter
		self.start_location = self.location_exist(start_location)
		self.end_location = self.location_exist(end_location)
		self.weight_kg = weight_kg
		self.contact_information = contact_information
		self.check_weight(weight_kg)
		self._package_status = PackageStatus.PENDING
		self.assigned_truck = None

	def assign_to_truck(self, truck):
		self.assigned_truck = truck
		truck.assigned_packages.append(self)
		truck.current_load += self.weight_kg

	@property
	def package_status(self):
		return self._package_status

	def set_status(self, new_status):
		if new_status in PackageStatus.package_status:
			self._package_status = new_status


	def location_exist(self, location):
		if location in Package.LOCATION_MAPPING:
			return Package.LOCATION_MAPPING[location]
		elif location in Package.LOCATION_ABBR_MAPPING:
			return location
		else:
			raise ValueError('Invalid location!')

	def check_weight(self, value):
		value = try_parse_int(value)
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
		additional_stops = Route.valid_distances(0, 1)

		return (
        "\n📦 PACKAGE DETAILS\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    f"🆔 ID                 : {self.package_id_count}\n"
    f"📍 Start Location     : {start_full_name}\n"
    f"📍 End Location       : {end_full_name}\n"
    f"📦⚖️ Weight           : {self.weight_kg} kg\n"
    f"📋 Contact Info       : {self.contact_information}\n"
    f"✅ Current Status     : {self._package_status}\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
)

