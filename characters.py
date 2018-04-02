# character classes should be put here later for better organization i guess
# like mario/player, peach, and donkey kong classes.
# also enemy classes like barrels, fireballs, etc.
import pygame, sys, time, board, random
from pygame.locals import *
vec = pygame.math.Vector2

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pygameg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player: # player class. could possible change this to have options to have different players/colors
    # need to add conditions so doesnt go through structures/walls/platforms
    # CONDITIONS SHOULD USE collidepoint function call with rectangles and stuff i think

    def __init__(self, surface):
        self.surface = surface
        self.surface_size = self.surface.get_size()
        self.color = pygame.Color('red')
        self.rect = Rect(0, self.surface_size[1] - 10, 10, 10)


        self.vel = vec(0, 0)
        self.acc = vec(0, 0)


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

    def move_vert(self, rect, direction):
        size = self.surface.get_size()
        if direction < 0 and rect.top > 0:
                rect.y = rect.y + direction * 5
        if direction > 0 and rect.bottom < size[1]:
                rect.y = rect.y + direction * 5

    def move_horiz(self, rect, direction):
        size = self.surface.get_size()
        if direction < 0 and rect.left > 0:
            rect.x = rect.x + direction * 5
            #self.vx = -5
        if direction > 0 and rect.right < size[0]:
            rect.x = rect.x + direction * 5
            #self.vx = 5

    def jump(self):
        # # jump only if standing on a platform
        # self.rect.x += 1
        # hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        # self.rect.x -= 1
        # if hits:
        self.vel.y = -10

class Fireball:

    def __init__(self, surface):
        self.surface = surface
        self.radius = 5
        self.center = [20, 20]
        self.color = pygame.Color('orange')
        self.randomspeed = random.randint(1, 5)
        self.speed = [3, 4]
        self.surface_size = self.surface.get_size()

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

    def move(self): # add in more parameters/arguments when walls are drawn
        for coord in range(2):
            self.center[coord] = (self.center[coord] + self.speed[coord])

             # change direction if top or left
            if self.center[coord] < self.radius:
                self.speed[coord] = -self.speed[coord]

             # change direction if bottom or right
            if self.center[coord] + self.radius > self.surface_size[coord]:
                self.speed[coord] = -self.speed[coord]

class Peach:
    peachColor = pygame.Color('pink') # replace with sprite?

    def __init__(self, surface):
        self.surface = surface
        self.surface_size = self.surface.get_size()
        self.color = pygame.Color('pink')
        self.rect = Rect(self.surface_size[0] - 10, 0, 10, 10)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)

class DonkeyKong:
    kongColor = pygame.Color('brown')

    def __init__(self, surface):
        self.surface = surface
        self.radius = 10
        self.center = [20, 20]
        self.color = DonkeyKong.kongColor

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.center, self.radius, 0)
