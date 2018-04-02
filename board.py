import pygame, sys, time, board
from pygame.locals import *

class Board: # Melisse are u gonna work on this
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
        self.color = wallsColor



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
