from graph import Graph
from binary_heap import BinaryHeap
import math, pygame, sys
from chars import *

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

def findpath(playercoordx, playercoordy, blockx, blocky):
    # MODIFIED VERSION OF PROCESS_INPUT FROM ASSIGN 1 PART 1

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
clock = pygame.time.Clock()
time = pygame.time.get_ticks() // 1000 # divide to get in seconds
while True:
    if ((pygame.time.get_ticks() // 1000) - time) % 10 == 0:
        # when testing this out rmr to change speed of block to 0
        findpath(self.player.rect.x, self.player.rect.y, self.player.block.x, self.player.block.y)
