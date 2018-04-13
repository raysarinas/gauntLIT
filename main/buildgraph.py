from graph import Graph

import pygame

# WORK ON THIS LATER PROBABLY OR COULD INTEGRATE TO GRAPH.PY CLASS THAT ALREADY EXISTS? IDK IF HAVE TIME!
class Generator:

    def __init__(self, surface, walls, wall_list):
        self.screenwidth = self.surface.get_width()
        self.screenheight = self.surface.get_height()
        self.surface = surface
        self.splitnum = 25
        self.walls = walls
        self.wall_list = wall_list
        self.widthrange = (self.screenwidth - 10) // self.splitnum + 1
        self.heightrange = (self.screenheight - 10) // self.splitnum + 1
        self.location = {}
        self.vertices = []

    def make_vertices(vlist, xrange, yrange):
        '''
        Construct a list of vertices with appropriate screen/window size.
        Efficiency: If H and V are the number of horizontal and vertical vertices,
          the runtime is O (H * V).

        Args:
          vlist: An empty list that will store a returned list of vertices.
          xrange: The number of vertices that will be generated in the horizontal
            direction.
          yrange: The number of vertices that will be generated in the vertical
            direction.

        Returns:
          vlist: A list containing all the vertices attainble with the provided
            screen width and height.
        '''
        for x in range(1, xrange):
            for y in range(1, yrange):
                vlist.append([splitnum*i, splitnum*j])
        return vlist

    def filter_vertices(vertices, walls):
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
        vertexlist = [tuple(v) for v in vertices if v not in invalid]
        return vertexlist

    def make_edges(vertexlist):
        # make graph edges
        edges = []
        for i in range(len(vertexlist)):
            for j in range(len(vertexlist)):
                if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                    if vertexlist[i][1] != vertexlist[j][1]: # vertices in same column
                        if (vertexlist[i][1] + splitnum == vertexlist[j][1]): # if vertex beside i'th vertex
                            edges.append((vertexlist[i], vertexlist[j])) # ADD EDGE
                            edges.append((vertexlist[j], vertexlist[i])) # BOTH WAYS SO UNDIRECTED

                # REPEAT but with horiztonal vertices now i guess
                if vertexlist[i][1] == vertexlist[j][1]:
                    if vertexlist[i][0] != vertexlist[j][0]:
                        if vertexlist[i][0] + splitnum == vertexlist[j][0]:
                            edges.append((vertexlist[i], vertexlist[j]))
                            edges.append((vertexlist[j], vertexlist[i]))
        return edges

    def make(): # make/return the graph!
        pass



def generate_graph(surface, walls, wall_list):
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

    #invalidverts = {}
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

    # EDGES AND STUFFFFF

    ''' EDGE TESTING STARTS HERE '''
    #vertexlist = valid
    edges = []

    # CREATE THE EDGES OF THE GRAPH
    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] != vertexlist[j][1]: # vertices in same column
                #     # then this is just the vertex itself.
                #     pass
                # else: # vertices in same row but not same column. transverse row.
                    if (vertexlist[i][1] + splitnum == vertexlist[j][1]): # if vertex beside i'th vertex
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i])) # BOTH WAYS SO UNDIRECTED
                        #vedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], 2, (splitnum - 1)))
            # REPEAT but with horiztonal vertices now i guess
            if vertexlist[i][1] == vertexlist[j][1]:
                if vertexlist[i][0] != vertexlist[j][0]:
                #     pass #temp2.append(vertexlist[i]) # JUST TO CHECK
                # else:
                    if vertexlist[i][0] + splitnum == vertexlist[j][0]:
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        edges.append((vertexlist[j], vertexlist[i]))
                        #hedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], (splitnum - 1), 2))


    # GENERATE/MAKE THE GRAPH
    graph = Graph(set(vertexlist), edges) # initiate graph with set of vertices!
    v = graph.get_vertices()
    e = graph.get_edges()


    return graph, location #invalidverts, rects
