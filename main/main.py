import pygame
from walls import *
from chars import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.done = False
        self.cont = True
        self.all_sprite_list = pygame.sprite.Group()
        self.wall_list, self.all_sprite_list = makeWalls(self.all_sprite_list)
        self.player = Player(50, 50)
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(5, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -5)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, 5)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-5, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, 5)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -5)

    def play(self):
        while not self.done:
            self.handle_event()
            self.all_sprite_list.update()
            self.surface.fill(BLACK)
            self.all_sprite_list.draw(self.surface)
            pygame.display.flip()


def main():
    pygame.init() # initialize pygame
    surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # make screen
    pygame.display.set_caption('Mario Maze Apparently')
    game = Game(surface)
    game.play()

main()
pygame.quit()
