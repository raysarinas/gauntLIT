import pygame, random
import pygame.gfxdraw
from pathfinding import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

class Player(pygame.sprite.Sprite):
    """ This class the character Mario that that player controls
    controls. Subclass of "Sprite" class in Pygame."""

    # Constructor function
    # gets the starting position of mario
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
        self.sprite = pygame.image.load('images/luigi.gif')
        self.size = self.sprite.get_rect().size

        # Set height, width
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)

        # Make our top-left corner of the sprite the passed-in location.
        self.rect = self.image.get_rect()
        self.image.blit(self.sprite, self.rect)
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Peach(pygame.sprite.Sprite):
    """ This class represents Princess Peach that must be saved.
        Sprite is static and this class just represents the rectangle
        in which holds the image of Peach.
        Subclass of "Sprite" class in Pygame.
    """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.sprite = pygame.image.load('images/peach.png')
        self.size = self.sprite.get_rect().size
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.image.blit(self.sprite, self.rect)
        self.rect.y = y
        self.rect.x = x


class Ghost(pygame.sprite.Sprite):
    """
    This class represents the ghost.
    Subclass of "Sprite" class in Pygame.
    """

    def __init__(self, color, x, y):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.

        self.sprite = pygame.image.load('images/boo.gif')
        self.size = self.sprite.get_rect().size
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)

        # Fetch the rectangle object that has the dimensions of the image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.image.blit(self.sprite, self.rect)
        self.rect.x = 25
        self.rect.y = 25

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 10
        self.right_boundary = 10
        self.top_boundary = 550
        self.bottom_boundary = 350

        # Instance variables for ghost speed/direction
        self.change_x = 0
        self.change_y = 0

    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # make sure the player does not hit the right or left boundaries
        if self.rect.right >= self.right_boundary + 40 or self.rect.left <= self.left_boundary:
            self.change_x *= -1


        # make sure the player does not hit the top or bottom boundaries
        if self.rect.bottom - 40 >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1

    def update_x(self, reached, location, ghostcoord):
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

    def update_y(self, reached, location, ghostcoord):
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

    def moveghost(self, reached, location, player):
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
        delx = self.update_x(reached, location, self.rect.x)
        dely = self.update_y(reached, location, self.rect.y)

        if delx != None:
            self.rect.x = delx
        else:
            self.change_x = 0

        if dely != None:
            self.rect.y = dely
        else:
            self.change_y = 0
