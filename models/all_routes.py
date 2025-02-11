from models.route_matrix import Routes
class AllRoutes:


	@staticmethod
	def route_distance(routes):
		total_distance = 0
		for i in range(len(routes)-1):
			current_city = routes[i]
			next_city = routes[i +1]
			distance = Routes.my_distance(current_city,next_city)
			if distance is None:
				raise ValueError
			total_distance+=distance

		print(f"Routes: {'->'.join(routes)}")
		print(f"Total distance: {total_distance} km")
		return total_distance
course = ["DAR","SYD","MEL"]

AllRoutes.route_distance(course)