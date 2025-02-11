from models.route_matrix import Routes
class AllRoutes:

	# ROUTES = ['Sydney', 'Melboune', 'Adelaide', 'Perth']


	@staticmethod
	def km_distance(route):
		routes1 = ["SYD", "MEL", "ADL", "PER"]
		total_distance = 0
		for i in range(len(routes1)):
			current_city = routes1[i]
			next_city = routes1[i+1]
			if Routes.my_distance(current_city,next_city) in routes1:
				total_distance += Routes.my_distance(current_city, next_city)
			elif (next_city, current_city) in routes1:
				total_distance += Routes.my_distance(current_city, next_city)
			else:
				print("No")

		print(f"Routes: {'->'.join(route)}")
		print(f"Total distance: {total_distance} km")
		return total_distance
route = ["SYD", "MEL", "ADL", "PER"]

AllRoutes.km_distance(route)