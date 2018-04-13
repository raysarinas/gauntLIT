from chars import *
from pathfinding import *

def updateghost_x(reached, location, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][0] != ghostcoord:
            return location[reached[1]][0]

def updateghost_y(reached, location, ghostcoord):
    if len(reached) > 1:
        if location[reached[1]][1] != ghostcoord:
            return location[reached[1]][1]

def moveghost(reached, location, ghost, player):
    delx = updateghost_x(reached, location, ghost.rect.x)
    dely = updateghost_y(reached, location, ghost.rect.y)
    correction = 0

    if delx != None:
        if ghost.rect.x > player.rect.x:
            ghost.rect.x = delx - correction
        elif ghost.rect.x < player.rect.x:
            ghost.rect.x = delx + correction
    else:
        ghost.change_x = 0

    if dely != None:
        if ghost.rect.y > player.rect.y:
            ghost.rect.y = dely + correction
        elif ghost.rect.y < player.rect.y:
            ghost.rect.y = dely + correction
    else:
        ghost.change_y = 0
