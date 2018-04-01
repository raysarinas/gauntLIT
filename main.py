import pygame, sys, time, board
from pygame.locals import *

class Player: # player class. could possible change this to have options to have different players/colors
    # need to add conditions so doesnt go through structures/walls/platforms

    marioColor = pygame.Color('red')

    def __init__(self, surface):
        self.surface = surface
        self.radius = 7
        self.size = [10, 10]
        self.center = [10, surface.get_height() - 8]
        self.color = Player.marioColor
        self.what = pygame.Rect(100, self.surface.get_height() // 4, self.size[0], self.size[1])

    def draw(self):
        pygame.draw.rect(self.surface, Player.marioColor, self.what)
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)

class DonkeyKong:
    kongColor = pygame.Color('brown')

    def __init__(self, surface):
        self.surface = surface
        self.radius = 10
        self.center = [surface.get_width() - 20, 20]
        self.color = DonkeyKong.kongColor

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)

class Peach:
    peachColor = pygame.Color('pink') # replace with sprite?

    def __init__(self, surface):
        self.surface = surface
        self.radius = 5
        self.center = [surface.get_width() - 10, 10]
        self.color = Peach.peachColor

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)

class Game:
    # class attributes
    bgColor = pygame.Color('blue')
    ballColor = pygame.Color('white')

    def __init__(self, surface):
        self.surface = surface
        self.center = [surface.get_width() // 2, surface.get_height() // 2]
        self.radius = 10
        self.color = Game.ballColor
        self.moving = False
        self.player = Player(self.surface)

    def draw(self):
        # THIS SEEMS LIKE IT WILL GET TO BE TOO LONG IF WE NEED TO DRAW
        # TOO MANY THINGS. MIGHT NEED TO KEEP GAME CLASS IN DIFFERENT FILE
        # OR HAVE DRAW FUNCTION BE A SUBCLASS OR WHATEVER OR SOMETHING
        self.surface.fill(Game.bgColor)
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)
        #player = Player(self.surface)
        kong = DonkeyKong(self.surface)
        self.player.draw()
        kong.draw()
        peach = Peach(self.surface)
        peach.draw()

    def update(self):
        if False: # end of game condition
        # if player coordinates == coordinates of barrel/fireball:
            # game.gameOver()
            return True
        else: # update and draw objects / continue the game
            self.draw()
            self.player.draw()
            return False

def main():
    pygame.init() # initialize pygame

    # set window size, title, frame delay
    surfaceSize = [500, 400]
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
