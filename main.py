import pygame, sys, time
from pygame.locals import *

class Game:
    # class attributes
    bgColor = pygame.Color('black')
    ballColor = pygame.Color('white')

    def __init__(self, surface):
        self.surface = surface
        self.center = [surface.get_width() // 2, surface.get_height() // 2]
        self.radius = 10
        self.color = Game.ballColor
        self.moving = False

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)

    def update(self):
        if False: # end of game condition
            return True
        else: # update and draw objects
            self.draw()
            return False

def main():
    pygame.init() # initialize pygame

    # set window size, title, frame delay
    surfaceSize = [800, 600]
    windowTitle = '275 Project I Guess' # title
    frameDelay = 0.02 # smaller is faster

    # creating the pygame window thing
    surface = pygame.display.set_mode(surfaceSize, 0, 0)
    pygame.display.set_caption(windowTitle)

    # create and initialize objects
    gameOver = False
    game = Game(surface)
    game.draw() # draw objects
    pygame.display.update() # refresh display

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # handling additional events (see other files for how )

        gameOver = game.update()
        pygame.display.update() # refresh display
        time.sleep(frameDelay) # set frame speed by pausing b/w frames

main()
