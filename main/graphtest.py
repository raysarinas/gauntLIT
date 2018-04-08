from graph import Graph
import pygame

def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    xrange = (screenwidth - 10) // 25 + 1
    yrange = (screenheight - 10) // 25 + 1
    print(xrange, yrange)

    vertices = []
    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([25 * i, 25 * j])

    print(vertices)
    print('num of vertices: ', len(vertices))


    vertdict = {} # store ALL vertices in a dictionary
    for i in range(len(vertices)):
        vertdict[i] = vertices[i]


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
                    invalidverts[i] = v # SOMETHING WRONG WITH IDENTIFIERS HERE
                    # YEAH INDEXING IS JUST WRONG HERE
                    invalid.append(v)
                    rects.append(pygame.Rect(v[0], v[1], 4, 4))

    good = vertdict.values()
    good = list(good) # list of ALL VERTICES
    #good = [tuple(x) for x in good] # convert vertices to tuples so hashable(?)
    print(good)
    print('num of total vertices: ', len(good))
    print('num of total invalid: ', len(invalid))

    goodrects = [] # for printing the valid vertices
    good = [v for v in good if v not in invalid] # filter out invalid vertices
    for v in good: # appent valid vertices to goodrects so can draw out valid vertices
        goodrects.append(pygame.Rect(v[0], v[1], 4, 4))

    ''' ADDING VERTICES TO GRAPH'''
    good = [tuple(x) for x in good] # convert vertices to tuples so hashable?
    # need to do it after filtering out apparently?? idk why it wont work otherwise
    goodset = set(good)
    print('vertices', goodset)
    graph = Graph(goodset)
    graph.get_vertices() # I THINK THIS WORKS O.K.


    # NEED TO WORK WITH DICTIONARY
    print(len(good))
    vertexdict = {}
    for i in range(len(good)):
        vertexdict.update({i:good[i]})

    print(vertexdict)
    print(len(vertexdict))

    ''' EDGE TESTING STARTS HERE '''
    # vertexlist = list(goodset)
    # for i in range(len(goodset)):
    # 
    # for i, j in range(len(vertexdict)):
    #     graph.add_edge((i, j))
    #
    # print(graph.get_edges())
    # print('num of edges: ', len(graph.get_edges()))
    #
    #
    #


    print('NUM OF VALID VERTS:', len(good))

    # for i in range(len(vertdict.keys())):
    #     if i in invalidverts.keys():
    #         #print(i, vertdict[i])
    #         del vertdict[i]
    # #print(len(vertdict))

    return vertdict, rects, goodrects #invalidverts, rects


#generate_graph(600, 400)
