import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([16, 26])

        # sprite
        #self.image = pygame.image.load('mario.png').convert_alpha
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.sprite = pygame.image.load('mario.png')
        self.image.blit(self.sprite, self.rect)
        self.rect.y = y
        self.rect.x = x

        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y

    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Peach(pygame.sprite.Sprite):
    """ This class represents Princess Peach that must be saved I guess? """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([18, 32])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.sprite = pygame.image.load('peach.png')
        self.image.blit(self.sprite, self.rect)
        self.rect.y = y
        self.rect.x = x

    #     # Set speed vector
    #     self.change_x = 0
    #     self.change_y = 0
    #     self.walls = None
    #
    # def changespeed(self, x, y):
    #     """ Change the speed of the player. """
    #     self.change_x += x
    #     self.change_y += y

    def update(self):
        # PROBABLY WILL NEED END GAME CONDITIONS IN HERE?
        """ CHECK IF HIT PEACH """
        pass

        # # Check and see if we hit anything
        # block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        # for block in block_hit_list:
        #
        #     # Reset our position based on the top/bottom of the object.
        #     if self.rect.left == Game.player.rect.right:
        #     #     self.rect.bottom = block.rect.top
        #     # else:
        #     #     self.rect.top = block.rect.bottom
        #
        #         pygame.font.init() # you have to call this at the start,
        #                # if you want to use this module.
        #         myfont = pygame.font.SysFont('Comic Sans MS', 30)
        #         textsurface = myfont.render('<3', False, (0, 0, 0))
        #         self.image.blit(textsurface,(0,0))
