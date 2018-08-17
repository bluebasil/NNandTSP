import structures
import heuristic
import random
import sys

num_cities = 16
data_points = 1000

f = open(f"d{random.randint(0,99999)}.csv", "a")

for i in range(data_points):
    print(i)

    cities = []

    for c in range(num_cities):
        new_city = structures.city()
        new_city.name = c
        new_city.x = random.randint(0,100)
        new_city.y = random.randint(0,100)
        cities.append(new_city)

        f.write(f"{new_city.x},{new_city.y},")

    solution = heuristic.solve(cities)

    for p in solution:
        f.write(f"{p.name},")

    f.write(f"{i}\n")


f.close()





