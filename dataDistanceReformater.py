import structures
import heuristic
import random
import math
import sys

num_cities = 16

fi = open(f"allData.csv", "r")
fo = open(f"allDataReformated.csv", "w")

for line in fi:
    # populate list of cities
    cities = []
    line_contents = line.split(",")
    for c in range(num_cities):
        new_city = structures.city()
        new_city.name = c
        new_city.x = int(line_contents[c*2])
        new_city.y = int(line_contents[c*2 + 1])
        cities.append(new_city)
        fo.write(f"{line_contents[c*2]},{line_contents[c*2+1]},")

    path_distance = 0
    last_city = 0
    total_distance_to = [0]*(num_cities-1)
    for i in range(num_cities*2 + 1, num_cities*3):
        path_distance += structures.distance(cities[last_city],cities[int(line_contents[i])])
        last_city = int(line_contents[i])
        total_distance_to[last_city - 1] = path_distance

    for i in total_distance_to:
        fo.write(f"{i},")

    # loop last to calculate total distance
    #print(int(line_contents[num_cities*2]))
    path_distance += structures.distance(cities[0],cities[int(line_contents[num_cities*3 - 1])])
    fo.write(f"{path_distance}\n")

fo.close()
fi.close()