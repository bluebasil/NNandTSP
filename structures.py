import math

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

def distance(city1, city2):
    return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)