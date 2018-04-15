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
    vertices: A list containing ALL vertices generated from the screen. Contains
    both valid and invalid vertices; used for completeness and for use in
    creating a dictionary attached to identifiers.
    vertexlist: A list containing all the vertices that are valid for both
    the player and ghost to move around/near/on.
    '''

    splitnum = 25
    xrange = (surface.get_width() - 10) // splitnum + 1
    yrange = (surface.get_height() - 10) // splitnum + 1

    vertices = []
    for x in range(1, xrange):
        for y in range(1, yrange):
            vertices.append([splitnum*x, splitnum*y])

    # filter out invalid vertices / wall points
    topleft = [] # list holding top left coordinates of walls
    bottomright = [] # list holding bottom right coordinates of walls
    invalid = [] # list holding invalid vertices

    for w in range(len(walls)):
        startx, starty = walls[w][0], walls[w][1]
        endx, endy = startx + walls[w][2], starty + walls[w][3]
        topleft.append([startx, starty])
        bottomright.append([endx, endy])

    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft[i][0], bottomright[i][0]):
                if v[1] in range(topleft[i][1], bottomright[i][1]):
                    invalid.append(v)

    # filter out invalid vertices and convert each vertex to a tuple so hashable
    valid = [tuple(v) for v in vertices if v not in invalid]
    return valid, vertices

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

def get_vertdict(vertexlist):
    # create a dictionary containing the valid vertices. useful for having identifiers
    # attached to each vertex so can be used in path finding.
    location = []
    for i in range(len(vertexlist)):
        location[i] = (vertexlist[i][0], vertexlist[i][1])
    return location


def make_graph(surface, walls): # make/return the graph!

    validvertices, allvertices = make_vertices(surface, walls)
    edges = make_edges(validvertices)
    location = get_vertdict(allvertices)
    graph = Graph(set(vertices), edges) # initiate graph with set of vertices!

    return graph, location


def generate_graph(surface, walls):
    # GET VERTICES FOR THE ENTIRE SCREEN
    screenwidth = surface.get_width()
    screenheight = surface.get_height()
    splitnum = 25
    xrange = (screenwidth - 10) // splitnum + 1 # NUMBER OF HORIZONTAL VERTICES
    yrange = (screenheight - 10) // splitnum + 1 # NUMBER OF VERTICAL VERTICES
    location = {}

    vertices = [] # ARRAY TO HOLD VERTICES
    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([splitnum * i, splitnum * j]) # APPEND VERTICE

    for i in range(len(vertices)):
        location[i] = (vertices[i][0], vertices[i][1])


    # STORE WALLS IN LISTS
    # ONE LIST TO HOLD TOP LEFT CORNER BOUNDARIES AND ANOTHER FOR BOTTOM RIGHT
    topleft_bounds = []
    bottomright_bounds = []
    for k in range(len(walls)):
        startx, starty = walls[k][0], walls[k][1] # top left coords
        width, height = walls[k][2], walls[k][3] # size of rects
        xbound, ybound = startx+width, starty+height # bottom left coords
        topleft_bounds.append([startx, starty])
        bottomright_bounds.append([xbound, ybound])

    invalid = []

    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft_bounds[i][0], bottomright_bounds[i][0]):
                if v[1] in range(topleft_bounds[i][1], bottomright_bounds[i][1]):
                    invalid.append(v)

    # GET VALID VERTICES AND FILTER OUT INVALID VERTICES
    # validrects = []
    vertexlist = [tuple(v) for v in vertices if v not in invalid]
    # filter out invalid vertices and convert to tuple so hashable
    # need to make hashable AFTER filtering out or else cant filter out in first place

    #vertexlist = valid
    edges = []

    # CREATE THE EDGES OF THE GRAPH
    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] != vertexlist[j][1]: # vertices in same column
                    if (vertexlist[i][1] + splitnum == vertexlist[j][1]): # if vertex beside i'th vertex
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i])) # BOTH WAYS SO UNDIRECTED
            # REPEAT but with horiztonal vertices now i guess
            if vertexlist[i][1] == vertexlist[j][1]:
                if vertexlist[i][0] != vertexlist[j][0]:
                    if vertexlist[i][0] + splitnum == vertexlist[j][0]:
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i]))

    # GENERATE/MAKE THE GRAPH
    graph = Graph(set(vertexlist), edges) # initiate graph with set of vertices!
    v = graph.get_vertices()
    e = graph.get_edges()


    return graph, location #invalidverts, rects
