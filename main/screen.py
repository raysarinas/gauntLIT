def finishScreen(game, winGame):
    if winGame:
        game.surface.fill(BLK)
        game.surface.blit(pygame.image.load('images/sunset.png'), game.surface.get_rect())
        winpic = pygame.image.load('images/win.png')
        game.surface.blit(winpic, [game.surface.get_width()//2 + 70, 70])

        fontWin = pygame.font.SysFont(None, 45, True)
        textWin = fontWin.render('YOU WIN!', True, pygame.Color('white'))
        textWin_rect = textWin.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        game.surface.blit(textWin, textWin_rect)

        fontAsk = pygame.font.SysFont(None, 100, True)
        textAsk = fontWin.render('Play Again? Press Space', True, pygame.Color('white'))
        textAsk_rect = textAsk.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
        game.surface.blit(textAsk, textAsk_rect)

    else:
        game.surface.fill(BLK)
        losepic = pygame.image.load('images/gameover.png')
        picrect = losepic.get_rect()
        game.surface.blit(losepic, ((game.surface.get_width() - picrect[0]) // 2, 2))

        fontWin = pygame.font.SysFont(None, 45, True)
        textWin = fontWin.render('GAME OVER', True, pygame.Color('white'))
        textWin_rect = textWin.get_rect(center=(SCREEN_WIDTH/2 - 40, SCREEN_HEIGHT/2 - 30))
        game.surface.blit(textWin, textWin_rect)

        fontAsk = pygame.font.SysFont(None, 100, True)
        textAsk = fontWin.render('Play Again? Press Space', True, pygame.Color('white'))
        textAsk_rect = textAsk.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
        game.surface.blit(textAsk, textAsk_rect)

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
                newgame = Game(game.surface)
                newgame.startScreen()

def startScreen(game):
    game.surface.blit(pygame.image.load('images/house.png'), game.surface.get_rect())

    fontwelcome = pygame.font.SysFont(None, 35, True)
    textwelcome = fontwelcome.render("HAUNTED BUNGALOW RESCUE", True, pygame.Color('white'))
    text_rect = textwelcome.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 100))
    game.surface.blit(textwelcome, text_rect)

    fontstart = pygame.font.SysFont(None, 30, True)
    textstart = fontstart.render('Press 1, 2, or 3 to Select a Difficulty', True, pygame.Color('white'))
    start_rect = textstart.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 70))
    game.surface.blit(textstart, start_rect)

    fontstart1 = pygame.font.SysFont(None, 30, True)
    textstart1 = fontstart1.render('1 - Easy', True, pygame.Color('white'))
    start_rect1 = textstart1.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 10))
    game.surface.blit(textstart1, start_rect1)

    fontstart2 = pygame.font.SysFont(None, 30, True)
    textstart2 = fontstart2.render('2 - Medium', True, pygame.Color('white'))
    start_rect2 = textstart2.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20))
    game.surface.blit(textstart2, start_rect2)

    fontstart3 = pygame.font.SysFont(None, 30, True)
    textstart3 = fontstart3.render('3 - Hard', True, pygame.Color('white'))
    start_rect3 = textstart3.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
    game.surface.blit(textstart3, start_rect3)

    pygame.display.flip()

    waiting = True
    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                waiting = False
                game = Game(game.surface)
                game.ghostSpeed = 200
                game.play()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                waiting = False
                game = Game(game.surface)
                game.ghostSpeed = 150
                game.play()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                waiting = False
                game = Game(game.surface)
                game.ghostSpeed = 50
                game.play()
