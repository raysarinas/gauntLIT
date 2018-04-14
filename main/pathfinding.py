from graph import Graph
from binary_heap import BinaryHeap
import math

def distance(start, end):
    """
    Here, start and end are two tuples which represent two vertices.
    Returns the manhattan distance between these two vertices.
    """

    playerx, playery = start[0], start[1]
    ghostx, ghosty = end[0], end[1]

    man_dist = abs((playerx - ghostx)) + abs((playery - ghosty))
    return man_dist

def neighbour_identifier(nbr, location):
    """
    Takes in a neighbour of a vertex and dictionary of vertices and
    searchs for the key value attached to that neighbour and returns it.

    MORE EFFICIENT WAY OF DOING THIS IS BINARY SEARCH OR TOP-DOWN
    DYNAMIC PROGRAMMING
    """
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
    """
    *** NOTE: This function is a modified version of our previous ***
    *** implementation of Dijkstra's Algorithm from Assignment 1  ***
    *** Part 1. Comments in code indicate changes made.           ***

    Find and return a least cost path in graph from start vertex to dest vertex.

    Args:
    graph (Graph): The digraph defining the edges between the
    vertices.
    start: The vertex where the path starts. It is assumed
    that start is a vertex of graph.
    dest: The vertex where the path ends. It is assumed
    that dest is a vertex of graph.
    location: A dictionary containing all the vertices on the screen.
    Keys of location are identifiers holding the vertices as values.

    Returns:
    list: A potentially empty list (if no path can be found) of
    the vertices in the graph. If there was a path, the first
    vertex is always start, the last is always dest in the list.
    Any two consecutive vertices correspond to some edge in graph.
    """

    reached = {}
    events = BinaryHeap()
    events.insert((start, start), 0)

    while len(events) > 0:
        edge, time = events.popmin()
        if edge[1] not in reached:
            reached[edge[1]] = edge[0]
            for nbr in graph.neighbours(location[edge[1]]):
                # because each vertex in our graph is a tuple, we use tuples
                # instead of single values to find the neighbours of a vertex
                # then find the identifier/key value attached to nbr tuple and
                # insert into binary heap appropriately
                nbrID = neighbour_identifier(nbr, location)
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

def findpath(player, ghost, graph, location):
    """
    Finds the path list from the ghost to the player.
    Firsts takes an instance of a take the player sprite class and a ghost
    sprite class and gets their (x,y) coordinates into separate lists and
    appropriate variables. Then initiate the minplayer and minghost values as
    infinity and start and destination vertices as None. Then find the nearest
    vertex to the start and destination/end points requested.

    Args:
    playercoordx, playercoordy: player sprite coordinates.
    location: a dictionary mapping the identifier of a vertex to
      the pair (xposition, ypostiion) of coordinates for that vertex on the
      game screen.

    Returns the least cost path?
    """

    playercoords = [player.rect.x, player.rect.y]
    ghostcoords = [ghost.rect.x, ghost.rect.y]

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
