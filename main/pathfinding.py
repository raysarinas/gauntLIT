from graph import Graph
from binary_heap import BinaryHeap
import math, pygame, sys, random, time
from chars import *
from buildgraph import *
from collections import deque

def distance(start, end):
    """
    Here e is a pair (u,v) of vertices. / technically just an edge
    Returns the manhattan distance between the two vertices u and v.
    """

    playerx = start[0]
    playery = start[1]

    blockx = end[0]
    blocky = end[1]

    man_dist = abs((playerx - blockx)) + abs((playery - blocky))
    # print(playerx)
    return man_dist #, playerx

class CostDistance():
    """
    Creates an instance of the CostDistance class and stores the
    dictionary "location" as a member of this class.
    """
    def __init__(self, location):
        """
        Creates an instance of the CostDistance class and stores the
        dictionary "location" as a member of this class.
        """
        self.locDict = location

    def distance(self, start, end):
        """
        Here e is a pair (u,v) of vertices. / technically just an edge
        Returns the manhattan distance between the two vertices u and v.
        """

        playerx = start[0]
        playery = start[1]

        blockx = end[0]
        blocky = end[1]

        man_dist = abs((playerx - blockx)) + abs((playery - blocky))
        return man_dist #, playerx

def neighbour_identifier(nbr, location):
    for v in location:
        if location[v] == nbr:
            return v

def least_cost_path(graph, start, dest, cost, location):
    reached = {}
    events = BinaryHeap()
    events.insert((start, start), 0)
    print((start, start))

    while len(events) > 0:
        edge, time = events.popmin()
        if edge[1] not in reached:
            reached[edge[1]] = edge[0]
            for nbr in graph.neighbours(location[edge[1]]):
                nbrID = neighbour_identifier(nbr, location) # THIS MIGHT BE SLOW
                # LIKE FINDING NBR ID IS SLOW PROBABLY A FASTER WAY TO GET IT???
                events.insert((edge[1], nbrID), time + cost.distance(location[edge[1]], nbr))

    if dest not in reached:
        return []

    current = dest
    path = [current]

    while current != start:
        current = reached[current]
        path.append(current)

    path = path[::-1]
    return path


# this should be in an infinite loop prob in main game execution
def findpath(playercoordx, playercoordy, blockx, blocky, graph, location):
    # MODIFIED VERSION OF PROCESS_INPUT FROM ASSIGN 1 PART 1
    # SHOuLD TAKE PLAYER AND GHOST COORDINATES
    # COMPUTE MANHATTAN DISTANCE (CALL DISTANCE FUNCTION)
    # FIND NEAREST VERTICES TO BOTH POINTS
    # JUST PRINT TO TERMINAL START AND END VERTICES
    graph = graph
    if graph:
        print('got graph!') # make sure getting the graph

    playercoords= [playercoordx, playercoordy]
    ghostcoords = [blockx, blocky]

    minplayer = float('inf')
    minghost = float('inf')

    startV = None
    endV = None

    # find the nearest vertex to the start and destination/end points
    # that have been inputted/requested
    for key, vertex in location.items():
        currentvert = location[key]
        playervertdist = distance(currentvert, playercoords)
        if playervertdist < minplayer:
            minplayer = playervertdist
            minplayerID = key

        ghostvertdist = distance(currentvert, ghostcoords)
        if ghostvertdist < minghost:
            minghost = ghostvertdist
            minghostID = key

    print('player ID:', minplayerID, '/ playercoord:', location[minplayerID])
    print('ghost ID:', minghostID, '/ghostcoord:', location[minghostID])

    # PLACEHOLDER *HERE* FOR OLD PATHFINDING STUFF

    cost = CostDistance(location)
    #print(location)

    #print(reached)
    print('poop')
    #print(graph.neighbours(location[minplayerID]))
    #print(bellman_ford(graph.get_vertices(), graph.get_edges(), minplayerID))
    reached = least_cost_path(graph, minghostID, minplayerID, cost, location)
    print(reached)

    # print(minplayer)
    # print(minghost)
