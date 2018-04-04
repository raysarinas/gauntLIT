import pygame, sys, time, board
from pygame.locals import *


# # List to hold all the sprites
# all_sprite_list = pygame.sprite.Group()
#
# # Make the walls. (x_pos, y_pos, width, height)
# wall_list = pygame.sprite.Group()
# wall = Wall(0, 0, 10, 600)
# wall_list.add(wall)
# all_sprite_list.add(wall)
#
# wall = Wall(10, 0, 790, 10)
# wall_list.add(wall)
# all_sprite_list.add(wall)
#
# wall = Wall(10, 200, 100, 10)
# wall_list.add(wall)
# all_sprite_list.add(wall)


class Board:
    # this should just be the platforms I guess.
    # we could just work on making the game like a maze-type game?
    # idk jumping and stuff seems too hard to work with.
    structColor = pygame.Color('white')

    def __init__(self, surface):
        self.surface = surface
        self.color = structColor
        self.initialize()

    def initialize(self):
        self.makeWalls()
        self.makeFloors()
        self.makeLadders()

    def makeWalls(self):
        # build walls

        wallsColor = pygame.Color('black')
        self.wallColor = wallsColor
        #self.rect = Rect(0, self.surface_size[1] - 5, 5, 5)
        pygame.draw.rect(self.surface, BLACK, [100, 100, 400, 300])


    def makeFloors(self):
        # make floors
        pass

    def makeLadders(self):
        # make ladders? idk
        pass

    def makeCoins(self):
        # what i hope to do in the future
        # add coins so player can use it for points
        # more of a bonus feature if everything else is working
        pass

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
