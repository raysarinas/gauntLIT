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
    return man_dist #, playerx

def neighbour_identifier(nbr, location):
    # COULD IMPROVE THIS BY IMPLEMENTING A BINARY SEARCH THING OR
    # LIKE DYNAMIC PROGRAMMING MAYBE? IDK MAYBE DIVIDE AND CONQUER
    for v in location:
        if location[v] == nbr:
            return v
    # low = 0
    # high = len(location) - 1
    #
    # while (low <= high):
    #     mid = low + (high - low) // 2
    #
    #     if (location[mid])

def least_cost_path(graph, start, dest, location):
    reached = {}
    events = BinaryHeap()
    events.insert((start, start), 0)
    #print((start, start))

    while len(events) > 0:
        edge, time = events.popmin()
        if edge[1] not in reached:
            reached[edge[1]] = edge[0]
            for nbr in graph.neighbours(location[edge[1]]):
                nbrID = location.index(nbr) # THIS MIGHT BE SLOW
                # LIKE FINDING NBR ID IS SLOW PROBABLY A FASTER WAY TO GET IT???
                events.insert((edge[1], nbrID), time + distance(location[edge[1]], nbr))

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

    playercoords= [playercoordx, playercoordy]
    ghostcoords = [blockx, blocky]

    startV = None
    endV = None

    # find the nearest vertex to the start and destination/end points
    # that have been inputted/requested
    minplayer = float('inf')
    minghost = float('inf')
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

    reached = least_cost_path(graph, minghostID, minplayerID, location)
    return reached
