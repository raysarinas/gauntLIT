from chars import *
from pathfinding import *

def moveghost_x(reached, location, graph, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][0] != ghostcoord:
            return location[reached[1]][0]

def moveghost_y(reached, location, graph, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][1] != ghostcoord:
            return location[reached[1]][1]

def moveghost(reached, location, graph, ghost, player):
    delx = moveghost_x(reached, location, graph, ghost.rect.x)
    dely = moveghost_y(reached, location, graph, ghost.rect.y)
    correctionfactor = 0

    if delx != None:
        if ghost.rect.x > player.rect.x:
            player.rect.x = newghost




#self.ghost.changespeed(5, 0)
