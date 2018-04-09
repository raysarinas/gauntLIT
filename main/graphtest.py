from graph import Graph
from itertools import combinations

import pygame

def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    xrange = (screenwidth - 10) // 25 + 1
    yrange = (screenheight - 10) // 25 + 1
    print(xrange, yrange)

    vertices = []
    for i in range(xrange + 1):
        for j in range(yrange + 1):
            vertices.append([25 * i, 25 * j])

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
    print('valid vertices', good)
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
    print(len(vertdict))

    ''' EDGE TESTING STARTS HERE '''
    vertexlist = good #list(goodset)
    test = []

    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] == vertexlist[j][1]: # vertices in same column
                    # then this is just the vertex itself.
                    print('vertex is itself: ', vertexlist[i], vertexlist[j])
                else: # vertices in same row but not same column. transverse row.
                    if vertexlist[i][1] + 25 == vertexlist[j][1]: # if vertex beside i'th vertex
                        # ADD EDGE
                        #print(vertexlist[i], 'and', vertexlist[j], 'are adjacent')
                        test.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], 7, 7))






    # for i in range(len(goodset)):
    #     graph.add_edge(vertexlist[i])
    for i in range(1, len(vertexlist)):
        if vertexlist[i][0] == vertexlist[i][1] or vertexlist[i][1] == vertexlist[i-1][0]:
            pass

    nodes = ['A', 'B', 'C', 'D', 'E']
    edges = list(combinations(good, 2))
    for i in range(len(edges)):
        graph.add_edge(edges[i])
    #print(list(edges))
    print(len(edges))
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

    return vertdict, rects, goodrects, test #invalidverts, rects


#generate_graph(600, 400)
