from chars import *
from pathfinding import *

def moveghost_x(reached, location, graph, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][0] != ghostcoord:
            return location[reached[1]][0]
        # for v in reached:
        #     print(location[v][0], location[v][1])
        #     if (ghostcoord != location[v][0]):
        #         return location[v][0]
        #     else:
        #         return 0
            # if (ghostcoord == location[v][0]) and (ghostcoord != location[v][1]):
            #     return location[v][1]

def moveghost_y(reached, location, graph, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][1] != ghostcoord:
            return location[reached[1]][1]
        #for v in reached:
            # print(location[v][0], location[v][1])
            # if (ghostcoord != location[v][1]):
            #     return location[v][1]
            # else:
            #     return 0
            # if (ghostcoord == location[v][0]) and (ghostcoord != location[v][1]):
            #     return location[v][1]



#self.ghost.changespeed(5, 0)
