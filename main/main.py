import pygame, random
import pygame.gfxdraw
from walls import *
from chars import *
from buildgraph import *
from pathfinding import *
from moveghost import *

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
        self.all_sprite_list = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()

        for i in range(1):
            self.block = Block(BLACK, 25, 25)
            self.block.rect.x = 25
            self.block.rect.y = 25
            self.block.left_boundary = 10
            self.block.top_boundary = 10
            self.block.right_boundary = 550
            self.block.bottom_boundary = 350
            self.all_sprite_list.add(self.block)
            self.block_list.add(self.block)

        self.peach = Peach(590 - 18, 15)
        self.all_sprite_list.add(self.peach)

        #self.wall_list, self.all_sprite_list = makeWalls(self.all_sprite_list)
        self.wall_list, self.all_sprite_list, self.walls = generate_walls(self.all_sprite_list)
        #print(self.walls)
        # FOR TESTING VERTICES AND GRAPH STUFF
        self.valid, self.badrects, self.goodrects, self.vedges, self.hedges, self.graph, self.location = generate_graph(self.surface, SCREEN_WIDTH, SCREEN_HEIGHT, self.walls, self.wall_list)

        self.player = Player(10, SCREEN_HEIGHT - 34)
        self.playerspeed = 4
        self.player.walls = self.wall_list
        self.all_sprite_list.add(self.player)
        self.ghostSpeed1 = 300
        self.ghostSpeed2 = 200
        self.ghostSpeed3 = 150

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
        #hitGhost = pygame.sprite.collide_rect(self.player, self.block)
        if hitPeach:
            #self.done
            winGame = True
            self.finishScreen(winGame)

        hitGhost1 = pygame.sprite.collide_rect(self.player, self.block)
        hitGhost2 = pygame.sprite.collide_rect(self.block, self.player)
# COLLISION IS TOO CLOSE LIKE
   # STILL PRETTY FAR FROM LUIGI AND STILL A COLLISION IS DETECTED?
   # get the range of coordinates for the player and the ghost, see if any
   # of them intersect and if they do, then that is when hitghost goes to finish screen

        playercoords = self.player.rect.x, self.player.rect.y
        ghostcoords = self.block.rect.x, self.block.rect.y
        if hitGhost1 or hitGhost2:
            winGame = False
            # print('player coords', self.player.rect.x, self.player.rect.y)
            # print('player size', self.player.size)
            # print('player rightside coordinates', self.player.rect.x + self.player.size[0], self.player.rect.y + self.player.size[1])
            # print('ghost coords', self.block.rect.x, self.block.rect.y)
            # print('ghost size', self.block.size)
            # print('ghost rightside coordinates', self.block.rect.x + self.block.size[0], self.block.rect.y + self.block.size[1])
            if (playercoords[0] != ghostcoords[0]):
                self.block.rect.x += 2
                self.block.update()
                self.surface.blit(pygame.image.load('images/moon.png'), self.surface.get_rect())
                self.all_sprite_list.draw(self.surface)
            if (playercoords[1] != ghostcoords[1]):
                self.block.rect.y += 5
                self.block.update()
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
            # self.surface.fill(BLACK)
            # self.surface.blit(pygame.image.load('images/moon.png'), self.surface.get_rect())
            blocks_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)
            self.all_sprite_list.draw(self.surface)

            time_since_path_last_found += dt
            # dt is measured in milliseconds, therefore 1000 ms = 1 seconds
            path = []
            if time_since_path_last_found > 200: # find coordinates every 2 seconds
                path = findpath(self.player.rect.x, self.player.rect.y, self.block.rect.x, self.block.rect.y, self.graph, self.location)
                time_since_path_last_found = 0 # reset it to 0 so you can count again

            newghostx = moveghost_x(path, self.location, self.graph, self.block.rect.x)
            newghosty = moveghost_y(path, self.location, self.graph, self.block.rect.y)
            correction = 0
            if newghostx != None:
                if self.block.rect.x > self.player.rect.x:
                    #print('change ghost x coord to:', newghostx)
                    self.block.rect.x = newghostx - correction
                elif self.block.rect.x < self.player.rect.x:
                    self.block.rect.x = newghostx + correction
            else:
                self.block.change_x = 0
                #self.block.rect.x = newghostx
            if newghosty != None:
                #self.block.change_y = newghosty
                if self.block.rect.y > self.player.rect.y:
                    #print('change ghost y coord to:', newghosty)
                    self.block.rect.y = newghosty + correction
                elif self.block.rect.y < self.player.rect.y:
                    self.block.rect.y = newghosty - correction
            else:
                self.block.change_y = 0

            # DRAW VERTICES ON TOP OF EVERYTHING
            # for rect in self.badrects:
            #     pygame.draw.rect(self.surface, pygame.Color('red'), rect)
            # for rect in self.goodrects:
            #     pygame.draw.rect(self.surface, pygame.Color('green'), rect)
            # for rect in self.vedges:
            #     pygame.draw.rect(self.surface, pygame.Color('orange'), rect)
            # for rect in self.hedges:
            #     pygame.draw.rect(self.surface, pygame.Color('purple'), rect)

            pygame.display.flip()
            self.collision()

    def finishScreen(self, winGame):
        if winGame:
            #print('win!')
            self.surface.fill(BLK)
            self.surface.blit(pygame.image.load('images/sunset.png'), self.surface.get_rect())
            winpic = pygame.image.load('images/win.png')
            self.surface.blit(winpic, [self.surface.get_width()//2 + 70, 70])
            #print(self.surface.get_rect())

            fontWin = pygame.font.SysFont(None, 45, True)
            textWin = fontWin.render('YOU WIN!', True, pygame.Color('white'))
            textWin_rect = textWin.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.surface.blit(textWin, textWin_rect)


            fontAsk = pygame.font.SysFont(None, 100, True)
            textAsk = fontWin.render('Play Again? Press Space', True, pygame.Color('white'))
            textAsk_rect = textAsk.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
            self.surface.blit(textAsk, textAsk_rect)

        else:
            #print('lose!')
            self.surface.fill(BLK)
            losepic = pygame.image.load('images/gameover.png')
            picrect = losepic.get_rect()
            self.surface.blit(losepic, ((self.surface.get_width() - picrect[0]) // 2, 2))
            #print(self.surface.get_rect())

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
        #self.surface.fill(BLUE)
        self.surface.blit(pygame.image.load('images/house.png'), self.surface.get_rect())

        fontwelcome = pygame.font.SysFont(None, 35, True)
        textwelcome = fontwelcome.render("HAUNTED BUNGALOW RESCUE", True, pygame.Color('white'))
        text_rect = textwelcome.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
        self.surface.blit(textwelcome, text_rect)
        #self.surface.blit(textwelcome, ((self.surface.get_width()/2)-175, (self.surface.get_height()/2)/2 - 30))

        fontstart = pygame.font.SysFont(None, 30, True)
        textstart = fontstart.render('Press 1, 2, or 3 to Select a Difficulty', True, pygame.Color('white'))
        start_rect = textstart.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 70))
        self.surface.blit(textstart, start_rect)
        #self.surface.blit(textstart, ((self.surface.get_width()/2)-175, (self.surface.get_height()/2)/2))

        fontstart1 = pygame.font.SysFont(None, 30, True)
        textstart1 = fontstart1.render('1 - Easy', True, pygame.Color('white'))
        start_rect1 = textstart1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 10))
        self.surface.blit(textstart1, start_rect1)
        #self.surface.blit(textstart1, ((self.surface.get_width()/2)-170, ((self.surface.get_height()/2)/2)+40))

        fontstart2 = pygame.font.SysFont(None, 30, True)
        textstart2 = fontstart2.render('2 - Medium', True, pygame.Color('white'))
        start_rect2 = textstart2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
        self.surface.blit(textstart2, start_rect2)
        #self.surface.blit(textstart2, ((self.surface.get_width()/2)-170, ((self.surface.get_height()/2)/2)+80))

        fontstart3 = pygame.font.SysFont(None, 30, True)
        textstart3 = fontstart3.render('3 - Hard', True, pygame.Color('white'))
        start_rect3 = textstart3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
        self.surface.blit(textstart3, start_rect3)
        #self.surface.blit(textstart3, ((self.surface.get_width()/2)-170, ((self.surface.get_height()/2)/2)+120))

        pygame.display.flip()

        waiting = True
        while waiting:
            #print("start")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 300
                    game.play()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 200
                    game.play()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    waiting = False
                    game = Game(self.surface)
                    game.ghostSpeed = 100
                    game.play()

        # game = Game(self.surface)
        # game.play()


        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #         newgame = Game(self.surface)
        #         newgame.play()
def main():
    pygame.init() # initialize pygame
    pygame.font.init() # for drawing words and stuff mayhaps?
    surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) # make screen
    pygame.display.set_caption("Green Mario's Haunted Bungalow Rescue")


    game = Game(surface)
    #game.play()
    game.startScreen()

main()
pygame.quit()
