from chars import *
from pathfinding import *

def updateghost_x(reached, location, ghostcoord):
    '''
    Update the x-coordinate/position of the ghost. If length of shortest
    path to the player isn't empty and the ghost isn't at the vertex closest
    to the player, then move the ghost to the next vertex part of the shortest
    path.

    Args:
    reached: A list containing all the vertices in the 'least cost path'.
    location: A dictionary containing all the vertices as tuples on the
    screen with identifiers as keys for the vertices.
    ghostcoord: Coordinate (tuple) of the current x-coordinate/position of
    the ghost.

    Returns: Tuple containing the x-coordinate to move ghost to.
    '''
    if len(reached) > 1:
        if location[reached[1]][0] != ghostcoord:
            return location[reached[1]][0]

def updateghost_y(reached, location, ghostcoord):
    '''
    Update the y-coordinate/position of the ghost. If length of shortest
    path to the player isn't empty and the ghost isn't at the vertex closest
    to the player, then move the ghost to the next vertex part of the shortest
    path.

    Args:
    reached: A list containing all the vertices in the 'least cost path'.
    location: A dictionary containing all the vertices as tuples on the
    screen with identifiers as keys for the vertices.
    ghostcoord: Coordinate (tuple) of the current y-coordinate/position of
    the ghost.

    Returns: Tuple containing the y-coordinate to move ghost to.
    '''
    if len(reached) > 1:
        if location[reached[1]][1] != ghostcoord:
            return location[reached[1]][1]

def moveghost(reached, location, ghost, player):
    '''
    Move the ghost sprite on the screen using a least cost path. Calls functions
    that will update the (x,y) coordinates/position of the ghost sprite and checks
    if the path from the ghost to the player is empty or not. If not empty, these
    functions return the new (x,y) coordinates to move the ghost. This function will
    then update the ghost position on the screen.

    Args:
    reached: A list containing all the vertices in the 'least cost path'.
    location: A dictionary containing all the vertices as tuples on the
    screen with identifiers as keys for the vertices.
    ghost: An instance of a ghost sprite object.
    player: An instance of a player sprite object.

    Returns: None
    '''
    delx = updateghost_x(reached, location, ghost.rect.x)
    dely = updateghost_y(reached, location, ghost.rect.y)


    if delx != None:
        ghost.rect.x = delx
    else:
        ghost.change_x = 0

    if dely != None:
        ghost.rect.y = dely
    else:
        ghost.change_y = 0
