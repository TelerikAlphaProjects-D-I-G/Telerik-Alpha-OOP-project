from models.route_matrix import Routes


class AllRoutes:

	total_distance = 0

	@staticmethod
	def route_distance(routes):
		total_distance = 0
		for i in range(len(routes)-1):
			current_city = routes[i]
			next_city = routes[i +1]
			distance = Routes.my_distance(current_city,next_city)
			if distance is None:
				raise ValueError
			AllRoutes.total_distance+=distance

		return AllRoutes.total_distance

# course = ["DAR","SYD"]
#
# print(AllRoutes.route_distance(course))
