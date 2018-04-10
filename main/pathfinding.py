from graph import Graph
from binary_heap import BinaryHeap
import math, pygame, sys
from chars import *
from graphtest import *

# ******************************
# PLEASE IMPLEMENT THE PATHFINDING STUFF IN THE FINDPATH FUNCTION NOT THE
# GETPATH FUNCTION!!!!!
# ******************************
def distance(self, e):
    """
    Here e is a pair (u,v) of vertices. / technically just an edge
    Returns the manhattan distance between the two vertices u and v.
    """
    lon1, lat1 = e[0][0], e[0][1]
    lon2, lat2 = e[1][0], e[1][0]

    # calculate the manhattan distance between two points(x1,y1) and (x2,y2)
    e_dist = abs((lat2 - lat1)) + abs((lon2 - lon1))
    return e_dist

def getpath(playercoordx, playercoordy, blockx, blocky):

    # STILL NEED TO EDIT TO FIT OUR PROJECT NOT SURE HOW TO DO THAT YET!
    # store list of input things into appropriate variables
    valid = request[0]
    startcoord = [int(request[1]), int(request[2])]
    destination = [int(request[3]), int(request[4])]

    # initialize minimum start/end and start/end vertex values
    minStart = float('inf')
    minEnd = float('inf')
    startV = None
    endV = None

    # check if a valid request has been inputted
    checkrequest(valid)

    # find the nearest vertex to the start and destination/end points
    # that have been inputted/requested
    for vertex, point in location.items():
        startDist = euc_dist(point, startcoord)
        endDist = euc_dist(point, destination)
        if startDist <= minStart:
            startV = vertex
            minStart = startDist
        if endDist <= minEnd:
            endV = vertex
            minEnd = endDist

    return startV, endV


# this should be in an infinite loop prob in main game execution

def findpath(playercoordx, playercoordy, blockx, blocky, graph):
    # MODIFIED VERSION OF PROCESS_INPUT FROM ASSIGN 1 PART 1
    # SHOuLD TAKE PLAYER AND GHOST COORDINATES
    # COMPUTE MANHATTAN DISTANCE (CALL DISTANCE FUNCTION)
    # FIND NEAREST VERTICES TO BOTH POINTS
    # JUST PRINT TO TERMINAL START AND END VERTICES
    graph = graph
    if graph:
        print('got graph!') # make sure getting the graph

    print('player coordinates:', playercoordx, playercoordy)
    print('ghost goordinates: ', blockx, blocky)
