from graph import Graph
import pygame

def generate_graph(surface, screenwidth, screenheight, walls, wall_list):
    graph = Graph
    xrange = (screenwidth - 10) // 25 + 1
    yrange = (screenheight - 10) // 25 + 1
    print(xrange, yrange)
    print(walls)
    vertices = []

    for i in range(1, xrange):
        for j in range(1, yrange):
            vertices.append([25 * i, 25 * j])

    print(vertices)
    print(len(vertices))

    # THIS MIGHT BE THE BETTER WAY TO GETTING THE VALID VERTICES? IDK
    validverts = {}
    rects = []

    for wall in wall_list:
        for i in range(len(vertices)):
            if wall.rect.collidepoint(vertices[i]):
                continue
            else:
                validverts[i] = vertices[i]
                rects.append(pygame.Rect(vertices[i][0], vertices[i][1], 1, 1))
                # pygame.draw.rect(surface, pygame.Color('red'), rect)

    print(validverts)
    return validverts, rects


    vertdict = {}

    for i in range(len(vertices)):
        vertdict[i] = vertices[i]

    #print(vertdict)

    topleft_bounds = []
    bottomright_bounds = []

    for k in range(len(walls)):
        startx, starty = walls[k][0], walls[k][1] # top left coords
        width, height = walls[k][2], walls[k][3] # size of rects
        xbound, ybound = startx+width, starty+height # bottom left coords
        topleft_bounds.append([startx, starty])
        bottomright_bounds.append([xbound, ybound])

    #print(topleft_bounds)
    #print(bottomright_bounds)

    valid = []

# something along these lines should implement algorithm that
# only adds valid vertices

# NEED TO FIX THIS???
    for v in vertices:
        for i in range(len(walls)):
            if v[0] in range(topleft_bounds[i][0], bottomright_bounds[i][0]):
                if v[1] in range(topleft_bounds[i][1], bottomright_bounds[i][1]):
                    pass
            else:
                pass #print(v)


        '''#if vertices[v][0] in range(topleft_bounds[0][0], bottomright_bounds[0][0]):
        if not True:    # ^^^^ THIS ISNT RIGHT I THINK
            pass
        else:
            print(v[0])
            valid.append(v)'''




#generate_graph(600, 400)
