import pygame, random, sys
import pygame.gfxdraw
from walls import *
from chars import *
from buildgraph import *
from pathfinding import *

# Colors
BLACK = (100, 10, 0)
BLK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (187, 192, 255)

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.done = False
        self.cont = True

        # INITIALIZE character sprites
        self.all_sprite_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()

        self.ghost = Ghost(BLACK, 25, 25)
        self.all_sprite_list.add(self.ghost)
        self.block_list.add(self.ghost)
        self.peach = Peach(590 - 18, 15)
        self.all_sprite_list.add(self.peach)

        self.wall_list, self.all_sprite_list, self.walls = generate_walls(self.all_sprite_list)
        #print(self.walls)
        # FOR TESTING VERTICES AND GRAPH STUFF
        self.graph, self.location = make_graph(self.surface, self.walls)

        self.player = Player(10, SCREEN_HEIGHT - 34)
        self.playerspeed = 4
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player)
        self.ghostSpeed = 200

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-self.playerspeed, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(self.playerspeed, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, -self.playerspeed)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, self.playerspeed)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(self.playerspeed, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-self.playerspeed, 0)
                elif event.key == pygame.K_UP:
                    self.player.changespeed(0, self.playerspeed)
                elif event.key == pygame.K_DOWN:
                    self.player.changespeed(0, -self.playerspeed)

    # DETECT COLLISION
    def collision(self):
        winGame = False
        # player collision with peach
        hitPeach = pygame.sprite.collide_rect(self.player, self.peach)
        if hitPeach:
            #self.done
            winGame = True
            self.finishScreen(winGame)

        hitGhost1 = pygame.sprite.collide_rect(self.player, self.ghost)
        hitGhost2 = pygame.sprite.collide_rect(self.ghost, self.player)

        playercoords = self.player.rect.x, self.player.rect.y
        ghostcoords = self.ghost.rect.x, self.ghost.rect.y
        if hitGhost1 or hitGhost2:
            winGame = False
            if (playercoords[0] != ghostcoords[0]):
                self.ghost.rect.x += 2
                self.ghost.update()
                self.surface.blit(pygame.image.load('images/moon.png'), self.surface.get_rect())
                self.all_sprite_list.draw(self.surface)
            if (playercoords[1] != ghostcoords[1]):
                self.ghost.rect.y += 5
                self.ghost.update()
                self.surface.blit(pygame.image.load('images/moon.png'), self.surface.get_rect())
                self.all_sprite_list.draw(self.surface)
            self.finishScreen(winGame)

    def updatescreen(self):
        self.surface.fill(BLACK)
        self.surface.blit(pygame.image.load('images/moon.png'), self.surface.get_rect())

    def play(self):
        self.done = False
        time_since_path_last_found = 0
        clock = pygame.time.Clock()
        while not self.done:
            dt = clock.tick()
            self.handle_event()
            self.all_sprite_list.update()
            self.updatescreen()

            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            self.all_sprite_list.draw(self.surface)

            time_since_path_last_found += dt
            # dt is measured in milliseconds, therefore 1000 ms = 1 seconds
            path = []
            if time_since_path_last_found > self.ghostSpeed: # find coordinates every 2 seconds
                ghostloc, playerloc = findpath(self.player, self.ghost, self.graph, self.location)
                path = least_cost_path(self.graph, ghostloc, playerloc, self.location)
                time_since_path_last_found = 0 # reset it to 0 so you can count again

            #moveghost(path, self.location, self.ghost, self.player)
            self.ghost.moveghost(path, self.location, self.player)
            pygame.display.flip()
            self.collision()

    def finishScreen(self, winGame):
        if winGame:
            self.surface.fill(BLK)
            self.surface.blit(pygame.image.load('images/sunset.png'), self.surface.get_rect())
            winpic = pygame.image.load('images/win.png')
            self.surface.blit(winpic, [self.surface.get_width()//2 + 70, 70])

            fontWin = pygame.font.SysFont(None, 45, True)
            textWin = fontWin.render('YOU WIN!', True, pygame.Color('white'))
            textWin_rect = textWin.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.surface.blit(textWin, textWin_rect)

            fontAsk = pygame.font.SysFont(None, 100, True)
            textAsk = fontWin.render('Play Again? Press Space', True, pygame.Color('white'))
            textAsk_rect = textAsk.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
            self.surface.blit(textAsk, textAsk_rect)

        else:
            self.surface.fill(BLK)
            losepic = pygame.image.load('images/gameover.png')
            picrect = losepic.get_rect()
            self.surface.blit(losepic, ((self.surface.get_width() - picrect[0]) // 2, 2))

            fontWin = pygame.font.SysFont(None, 45, True)
            textWin = fontWin.render('GAME OVER', True, pygame.Color('white'))
            textWin_rect = textWin.get_rect(center=(SCREEN_WIDTH/2 - 40, SCREEN_HEIGHT/2 - 30))
            self.surface.blit(textWin, textWin_rect)

            fontAsk = pygame.font.SysFont(None, 100, True)
            textAsk = fontWin.render('Play Again? Press Space', True, pygame.Color('white'))
            textAsk_rect = textAsk.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
            self.surface.blit(textAsk, textAsk_rect)

        gameOver = False
        pygame.display.flip()
        waiting = True
        while waiting:
            #print('collided')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
                    newgame = Game(self.surface)
                    newgame.startScreen()

    def startScreen(self):
        self.surface.blit(pygame.image.load('images/house.png'), self.surface.get_rect())

        fontwelcome = pygame.font.SysFont(None, 35, True)
        textwelcome = fontwelcome.render("HAUNTED BUNGALOW RESCUE", True, pygame.Color('white'))
        text_rect = textwelcome.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
        self.surface.blit(textwelcome, text_rect)

        fontstart = pygame.font.SysFont(None, 30, True)
        textstart = fontstart.render('Press 1, 2, or 3 to Select a Difficulty', True, pygame.Color('white'))
        start_rect = textstart.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 70))
        self.surface.blit(textstart, start_rect)

        fontstart1 = pygame.font.SysFont(None, 30, True)
        textstart1 = fontstart1.render('1 - Easy', True, pygame.Color('white'))
        start_rect1 = textstart1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 10))
        self.surface.blit(textstart1, start_rect1)

        fontstart2 = pygame.font.SysFont(None, 30, True)
        textstart2 = fontstart2.render('2 - Medium', True, pygame.Color('white'))
        start_rect2 = textstart2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
        self.surface.blit(textstart2, start_rect2)

        fontstart3 = pygame.font.SysFont(None, 30, True)
        textstart3 = fontstart3.render('3 - Hard', True, pygame.Color('white'))
        start_rect3 = textstart3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
        self.surface.blit(textstart3, start_rect3)

        pygame.display.flip()

        waiting = True
        while waiting:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 200
                    game.play()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 150
                    game.play()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 50
                    game.play()

def main():
    pygame.init() # initialize pygame
    pygame.font.init() # for drawing words
    surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # make screen
    pygame.display.set_caption("Green Mario's Haunted Bungalow Rescue")

    game = Game(surface)
    game.startScreen()

main()
pygame.quit()
