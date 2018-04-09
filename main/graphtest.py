from graph import Graph

import pygame

def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    # GET VERTICES FOR THE ENTIRE SCREEN
    xrange = (screenwidth - 10) // 25 + 1 # NUMBER OF HORIZONTAL VERTICES
    yrange = (screenheight - 10) // 25 + 1 # NUMBER OF VERTICAL VERTICES
    print(xrange, yrange)

    vertices = [] # ARRAY TO HOLD VERTICES
    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([25 * i, 25 * j]) # APPEND VERTICE

    vertdict = {} # store ALL vertices in a dictionary
    for i in range(len(vertices)):
        vertdict[i] = vertices[i]

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



    # GETTING VALID VERTICES AND FILTERING
    validrects = []
    valid = [v for v in vertices if v not in invalid] # filter out invalid vertices
    for v in valid:
        validrects.append(pygame.Rect(v[0], v[1], 4, 4))

    # add vertices to the graph
    # convert vertices from lists to tuples so hashable?
    valid = [tuple(v) for v in valid]
    # need to make hashable AFTER filtering out or else cant filter out in first place
    validset = set(valid) # set of all valid vertices
    graph = Graph(validset) # initiate graph with set of vertices!
    v = graph.get_vertices()
    print(v) # this should work O.K.



    # EDGES AND STUFFFFF

    ''' EDGE TESTING STARTS HERE '''
    vertexlist = valid #good #list(goodset)
    vedges = [] # vertical vertices
    hedges = [] # horizontal vertices
    temp = []
    temp2 = []
    edges = []

    for i in range(len(vertexlist)):
        for j in range(len(vertexlist)):
            if vertexlist[i][0] == vertexlist[j][0]: # vertices in same row
                if vertexlist[i][1] == vertexlist[j][1]: # vertices in same column
                    # then this is just the vertex itself.
                    print('vertex is itself: ', vertexlist[i], vertexlist[j])
                    temp.append(vertexlist[i])
                else: # vertices in same row but not same column. transverse row.
                    if (vertexlist[i][1] + 25 == vertexlist[j][1]): # if vertex beside i'th vertex
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        vedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], 2, 24))
            # REPEAT but with horiztonal vertices now i guess
            if vertexlist[i][1] == vertexlist[j][1]:
                if vertexlist[i][0] == vertexlist[j][0]:
                    temp2.append(vertexlist[i])
                else:
                    if vertexlist[i][0] + 25 == vertexlist[j][0]:
                        # ADD EDGE
                        edges.append((vertexlist[i], vertexlist[j]))
                        hedges.append(pygame.Rect(vertexlist[i][0], vertexlist[i][1], 24, 2))


    print(temp)
    print('transvered vertices vertically:', len(temp))
    print(edges)
    print(len(edges))


    # for i in range(len(goodset)):
    #     graph.add_edge(vertexlist[i])
    for i in range(1, len(vertexlist)):
        if vertexlist[i][0] == vertexlist[i][1] or vertexlist[i][1] == vertexlist[i-1][0]:
            pass



    print('NUM OF VALID VERTS:', len(valid))
    print('NUM OF TOTAL VERTS:', len(vertices))

    # for i in range(len(vertdict.keys())):
    #     if i in invalidverts.keys():
    #         #print(i, vertdict[i])
    #         del vertdict[i]
    # #print(len(vertdict))

    return vertdict, rects, validrects, vedges, hedges #invalidverts, rects


#generate_graph(600, 400)
