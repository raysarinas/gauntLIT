import pygame, random
import pygame.gfxdraw
from walls import *
from chars import *
from graphtest import *
from pathfinding import *

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

        #self.wall_list, self.all_sprite_list = makeWalls(self.all_sprite_list)
        self.wall_list, self.all_sprite_list, self.walls = generate_walls(self.all_sprite_list)
        #print(self.walls)
        # FOR TESTING VERTICES AND GRAPH STUFF
        self.valid, self.badrects, self.goodrects, self.vedges, self.hedges, self.graph = generate_graph(self.surface, SCREEN_WIDTH, SCREEN_HEIGHT, self.walls, self.wall_list)

        self.player = Player(10, SCREEN_HEIGHT - 36)
        self.peach = Peach(590 - 18, 10)
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player, self.peach)

        for i in range(1):
            self.block = Block(BLACK, 25, 25)
            self.block.rect.x = 10 + i
            self.block.rect.y = 10 + i
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
        # player collision with peach
        hits = pygame.sprite.collide_rect(self.player, self.peach)
        if hits:
            self.done = True
            self.surface.fill(BLUE)
            #self.running = False

    def play(self):
        self.done = False
        time_since_path_last_found = 0
        clock = pygame.time.Clock()
        while not self.done:
            self.handle_event()
            self.all_sprite_list.update()
            self.surface.fill(BLACK)
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            for block in blocks_hit_list:
                print('hit!')
            self.all_sprite_list.draw(self.surface)

            # DRAW VERTICES ON TOP OF EVERYTHING
            for rect in self.badrects:
                pygame.draw.rect(self.surface, pygame.Color('red'), rect)
            for rect in self.goodrects:
                pygame.draw.rect(self.surface, pygame.Color('green'), rect)
            for rect in self.vedges:
                pygame.draw.rect(self.surface, pygame.Color('orange'), rect)
            for rect in self.hedges:
                pygame.draw.rect(self.surface, pygame.Color('purple'), rect)

            pygame.display.flip()
            self.collision()

            dt = clock.tick()

            time_since_path_last_found += dt
            # dt is measured in milliseconds, therefore 1000 ms = 1 seconds
            if time_since_path_last_found > 5000: # find coordinates every 2 seconds
                findpath(self.player.rect.x, self.player.rect.y, self.block.rect.x, self.block.rect.y, self.graph)
                time_since_path_last_found = 0 # reset it to 0 so you can count again


def main():
    pygame.init() # initialize pygame
    pygame.font.init() # for drawing words and stuff mayhaps?
    surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # make screen
    pygame.display.set_caption('Some sort of mario maze game I guess')
    game = Game(surface)
    game.play()

main()
pygame.quit()
