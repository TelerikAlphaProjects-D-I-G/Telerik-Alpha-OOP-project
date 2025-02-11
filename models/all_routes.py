from models.route_matrix import Routes
class AllRoutes:

	ROUTES = ['Sydney', 'Melboune', 'Adelaide', 'Perth']
	def km_distance(route):
		total_distance = 0
		for i in range(len(ROUTES) - 1):
			current_city = ROUTES[i]
			next_city = ROUTES[i+1]
			if (current_city, next_city) in AllRoutes.ROUTES:
				total_distance += AllRoutes.ROUTES[(current_city, next_city)]
			elif (next_city, current_city) in AllRoutes.ROUTES:
				total_distance += AllRoutes.ROUTES[(next_city, current_city)]
			else:
				print("No")
		print(f"Routes: {'->'.join(route)}")
		print(f"Total distance: {total_distance} km")
		return total_distance
route = ['Sydney', 'Melboune', 'Adelaide']
AllRoutes.km_distance(route)