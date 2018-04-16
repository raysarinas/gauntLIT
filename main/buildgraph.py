from graph import Graph
import pygame

'''
HELPER FUNCTIONS TO BUILD GRAPH UTILIZED IN THE GAME FOR GHOST MOVEMENT/A.I. STUFF
'''

def make_vertices(surface, walls): # NEED WALLS AS ARGUMENT
    '''
    Construct a list of vertices with appropriate screen/window size.
    Filter out invalid vertices, i.e. those that are part of/contained within
    walls/borders on the screen.
    Efficiency: If H and V are the number of horizontal and vertical vertices,
      the runtime is O (H * V).

    Args:
    surface: Pygame surface object
    walls: A list of wall coordinates and sizes parsed from a textfile.

    Returns:
    vertexlist: A list containing all the vertices that are valid for both
    the player and ghost to move around/near/on.
    location: A dictionary containing ALL vertices generated from the screen. Contains
    both valid and invalid vertices; used for completeness and for path finding to be able to
    identify vertices and corresponding neighbours with identifiers.
    '''

    splitnum = 25 # how much we will be dividing the screen by to make vertices
    # get ranges of x and y coordinates wrt to screen size
    xrange = (surface.get_width() - 10) // splitnum + 1
    yrange = (surface.get_height() - 10) // splitnum + 1

    # initiate empty list to store all possible vertices on screen
    vertices = []
    for x in range(1, xrange):
        for y in range(1, yrange):
            vertices.append([splitnum*x, splitnum*y])

    location = {}
    for i in range(len(vertices)):
        location[i] = (vertices[i][0], vertices[i][1])

    # filter out invalid vertices / wall points
    topleft = [] # list holding top left coordinates of walls
    bottomright = [] # list holding bottom right coordinates of walls
    invalid = [] # list holding invalid vertices

    for w in range(len(walls)):
        startx, starty = walls[w][0], walls[w][1]
        endx, endy = startx + walls[w][2], starty + walls[w][3]
        topleft.append([startx, starty])
        bottomright.append([endx, endy])

    # MORE EFFICIENT AND FASTER WAY OF FILTERING VERTICES WOULD/COULD INCLUDE USING
    # BINARY SEARCH JUST DIDN'T HAVE TIME TO IMPLEMENT
    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft[i][0], bottomright[i][0]):
                if v[1] in range(topleft[i][1], bottomright[i][1]):
                    invalid.append(v)

    # filter out invalid vertices and convert each vertex to a tuple so hashable
    valid = [tuple(v) for v in vertices if v not in invalid]
    return valid, location

def make_edges(vertexlist):
    '''
    Construct a list of edges from based on the vertices valid for the player
    and ghost to move through/around.

    Args:
    vertexlist: A list containing all the vertices that are valid for both
    the player and ghost to move around/near/on.

    Returns:
    edges: A list containing all the valid edges based on the vertices taken
    in as an argument (i.e. vertexlist).
    '''
    # make graph edges
    edges = []
    splitnum = 25
    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] != vertexlist[j][1]: # vertices in same column
                    if (vertexlist[i][1] + splitnum == vertexlist[j][1]): # if vertex beside i'th vertex
                        edges.append((vertexlist[i], vertexlist[j])) # ADD EDGE
                        edges.append((vertexlist[j], vertexlist[i])) # BOTH WAYS SO UNDIRECTED

            # REPEAT but with horiztonal vertices
            if vertexlist[i][1] == vertexlist[j][1]:
                if vertexlist[i][0] != vertexlist[j][0]:
                    if vertexlist[i][0] + splitnum == vertexlist[j][0]:
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i]))
    return edges

def make_graph(surface, walls): # make/return the graph!
    '''
    Just construct the graph used for gameplay.

    Args:
    surface: Pygame surface object
    walls: A list of wall coordinates and sizes parsed from a textfile.

    Returns:
    graph: An instance of a graph object containing vertices and edges.
    location: A dictionary containing ALL vertices generated from the screen. Contains
    both valid and invalid vertices; used for completeness and for path finding to be able to
    identify vertices and corresponding neighbours with identifiers.
    '''

    validvertices, location = make_vertices(surface, walls)
    edges = make_edges(validvertices)
    #location = get_vertdict(allvertices)
    graph = Graph(set(validvertices), edges) # initiate graph with set of vertices!

    return graph, location
