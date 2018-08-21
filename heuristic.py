import structures
from copy import deepcopy
import math
import sys

def printPath(path):
    for city in path:
        print(city.name)

def newCopyOfState(state):
    newState = stateClass
    newState.g = state.g
    newState.h = state.h
    newState.cities = deepcopy(state.cities)
    newState.path = deepcopy(state.path)
    return newState

def solve(cities):

    #keeps track of the number of states
    numNodes = 0

    path = []

    #add the first city to the path
    path.append(cities[0])
    cities.remove(cities[0])

    initalState = structures.stateClass(cities,path)
    initalState.g = 0

    stateList = []
    stateList.append(initalState)

    #stores the upper bound, which will also be the shortest path found so far
    upperCost = 999999
    upperState = None


    def sort(state):
        #sorting by the huristic slowed things down fractionally.
        #sorting implies that we will find lower bounds faster, so that we can ignore more branches
        return state.g #+ state.h

    #the recursive function
    def compute(state):
        nonlocal stateList
        #global start
        nonlocal upperCost
        nonlocal upperState
        nonlocal numNodes

        #print(stateList)
        #print(upperCost)


        if state.g > upperCost:
            #This will usually not be reached, because we prune these out before they are made
            return

        #add to tge number of states
        numNodes += 1

        if len(state.cities) < 1:
            #a new upper bound is found
            if state.g < upperCost:
                upperCost = state.g
                upperState = state
            return

        #We no longer check for timeout
        #check for timeout
        #current = time.time()
        #if current - start >=300:
        #   print("timeout... current length: " + str(upperCost))
        #   printPath(upperState.path)
        #   sys.exit()

        stateList = []

        #test all possible next cities
        for c in range(len(state.cities)):
            #although a state is temporarily created, it is really check feasibility, and may get destroyed later.
            #i wont count this as a new state (yet) because it is really just a temporary variable holder
            oldDist = structures.distance(state.path[-1],state.path[0])
            newState = structures.stateClass(state.cities[:],state.path[:])
            newState.g = state.g
            newState.h = 0
            newState.path.append(newState.cities[c])
            newState.cities.remove(newState.cities[c])
            #we remove the path from the last city to the first city (which created a cycle)
            fakeDist =  structures.distance(newState.path[-1], newState.path[0])
            #recalculate the new cyclic length
            newDist = structures.distance(newState.path[-2], newState.path[-1]) + fakeDist
            #this represents the cost of this path
            newState.g += newDist - oldDist

            #our heuristic.  its the distance to the farthest, un-connected city from both the last node and the first node
            #we know that this will always be less than or equal to the real distance because we have to connect that node somehow
            #the shortest possible way is if it was the last node left to connect and so we directly connect it to both te first and last node
            #to complete the cycle... and that distacne is exactly what the heuristic calculates
            maxDist = fakeDist
            to = None
            for r in newState.cities:
                d = structures.distance(newState.path[-1],r) + structures.distance(r,newState.path[0])
                if d > maxDist:
                    maxDist = d
                    to = r

            #This will always be positive
            newState.h = maxDist - fakeDist

            #if our huristic causes a cost over the upperBound, then we know that this course of action is perilious
            if upperCost >= newState.g + newState.h:
                stateList.append(newState)


        #sort by the current cost
        stateList.sort(key = sort)


        #recurse over all states
        for s in stateList:
            compute(s)

    #start recursion
    compute(initalState)

    return upperState.path

