from graph import Graph

import pygame

# WORK ON THIS LATER PROBABLY OR COULD INTEGRATE TO GRAPH.PY CLASS THAT ALREADY EXISTS? IDK IF HAVE TIME!
class Generator:

    def __init__(self, surface, screenwidth, screenheight, walls, wall_list):
        self.surface = surface
        self.splitnum = 25
        self.walls = walls
        self.wall_list = wall_list
        self.widthrange = (self.screenwidth - 10) // self.splitnum + 1
        self.heightrange = (self.screenheight - 10) // self.splitnum + 1
        self.location = {}
        self.vertices = []

    def make_vertices(vlist, xrange, yrange):
        for x in range(1, xrange):
            for y in range(1, yrange):
                vlist.append([splitnum*i, splitnum*j])

    def filter_vertices():
        pass
        # filter out invalid vertices / wall points

    def make_edges():
        pass
        # make graph edges

    def make(): # make/return the graph!
        pass


def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    # GET VERTICES FOR THE ENTIRE SCREEN
    splitnum = 25
    xrange = (screenwidth - 10) // splitnum + 1 # NUMBER OF HORIZONTAL VERTICES
    yrange = (screenheight - 10) // splitnum + 1 # NUMBER OF VERTICAL VERTICES
    location = {}
    #print(xrange, yrange)

    vertices = [] # ARRAY TO HOLD VERTICES
    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([splitnum * i, splitnum * j]) # APPEND VERTICE

    vertdict = {} # store ALL vertices in a dictionary
    for i in range(len(vertices)):
        vertdict[i] = vertices[i]
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

    invalidverts = {}
    invalid = []

# NEED TO FIX THIS???
    rects = [] # temp array to draw out invalid vertices
    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft_bounds[i][0], bottomright_bounds[i][0]):
                if v[1] in range(topleft_bounds[i][1], bottomright_bounds[i][1]):
                    invalid.append(v)
                    #invalid.append([v[0], v[1]])
                    rects.append(pygame.Rect(v[0], v[1], 4, 4))



    # GET VALID VERTICES AND FILTER OUT INVALID VERTICES
    validrects = []
    valid = [v for v in vertices if v not in invalid] # filter out invalid vertices
    for v in valid:
        validrects.append(pygame.Rect(v[0], v[1], 4, 4))

    # add vertices to the graph
    # convert vertices from lists to tuples so hashable?
    valid = [tuple(v) for v in valid]
    # need to make hashable AFTER filtering out or else cant filter out in first place
    validset = set(valid) # set of all valid vertices



    # EDGES AND STUFFFFF

    ''' EDGE TESTING STARTS HERE '''
    vertexlist = valid #good #list(goodset)
    vedges = [] # vertical vertices
    hedges = [] # horizontal vertices
    temp = []
    temp2 = []
    edges = []

    # CREATE THE EDGES OF THE GRAPH
    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] == vertexlist[j][1]: # vertices in same column
                    # then this is just the vertex itself.
                    temp.append(vertexlist[i]) # JUST TO CHECK
                else: # vertices in same row but not same column. transverse row.
                    if (vertexlist[i][1] + splitnum == vertexlist[j][1]): # if vertex beside i'th vertex
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i])) # BOTH WAYS SO UNDIRECTED
                        vedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], 2, (splitnum - 1)))
            # REPEAT but with horiztonal vertices now i guess
            if vertexlist[i][1] == vertexlist[j][1]:
                if vertexlist[i][0] == vertexlist[j][0]:
                    temp2.append(vertexlist[i]) # JUST TO CHECK
                else:
                    if vertexlist[i][0] + splitnum == vertexlist[j][0]:
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i]))
                        hedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], (splitnum - 1), 2))


    # GENERATE/MAKE THE GRAPH
    graph = Graph(validset, edges) # initiate graph with set of vertices!
    v = graph.get_vertices()
    e = graph.get_edges()


    return vertdict, rects, validrects, vedges, hedges, graph, location #invalidverts, rects


#generate_graph(600, 400)
