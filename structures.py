
class city:
	name = "_";
	x = 0
	y = 0

class stateClass:
	g = 0
	h = 0
	goal = False
	def __init__(self,cities,paths):
		self.cities = cities
		self.path = paths