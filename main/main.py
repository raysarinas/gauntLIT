import pygame, random
import pygame.gfxdraw
from walls import *
from chars import *

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.done = False
        self.cont = True
        self.all_sprite_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()

        self.wall_list, self.all_sprite_list = makeWalls(self.all_sprite_list)

        self.player = Player(10, SCREEN_HEIGHT - 36)
        self.peach = Peach(590 - 18, 10)
        self.fireball = Fireball(50, 50)
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player, self.peach, self.fireball)


        for i in range(50):
            self.block = Block(WHITE, 15, 15)
            self.block.rect.x = 20
            self.block.rect.y = 20
            self.block.left_boundary = 10
            self.block.top_boundary = 10
            self.block.right_boundary = 550
            self.block.bottom_boundary = 350
            self.all_sprite_list.add(self.block)
            self.block_list.add(self.block)

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


    # DETECT COLLISION
    def collision(self):
        # player collition with alien
        hits = pygame.sprite.collide_rect(self.player, self.peach)
        if hits:
            self.done = True
            screen.fill(BLUE)

            #self.running = False

    def play(self):
        self.done = False
        while not self.done:
            self.handle_event()
            self.all_sprite_list.update()
            self.surface.fill(BLACK)
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            for block in blocks_hit_list:
                print('hit!')
            self.all_sprite_list.draw(self.surface)
            pygame.display.flip()
            self.collision()


def main():
    pygame.init() # initialize pygame
    surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # make screen
    pygame.display.set_caption('Mario Maze Apparently')
    game = Game(surface)
    game.play()

main()
pygame.quit()
