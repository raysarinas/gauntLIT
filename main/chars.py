import pygame, random
import pygame.gfxdraw

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

class Player(pygame.sprite.Sprite):
    """ This class the character Mario that that player controls
    controls. """

    # Constructor function
    # gets the starting position of mario
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([16, 26])

        # sprite
        #self.image = pygame.image.load('mario.png').convert_alpha
        self.image.fill(BLACK)

        # Make our top-left corner of the sprite the passed-in location.
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

class Fireball(pygame.sprite.Sprite):
    """ BALL """

    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([25, 26])
        self.image.fill(BLACK)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.sprite = pygame.image.load('boo.png')
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


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.sprite = pygame.image.load('boo.png')
        self.image.blit(self.sprite, self.rect)

        # Instance variables that control the edges of where we bounce
        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        # Instance variables for our current speed and direction
        self.change_x = random.randint(1, 2)
        self.change_y = random.randint(1, 3)


    #def update(self):
        #self.rect.x += random.randint(1, 2)
        #self.rect.y += random.randint(2, 3)


    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary + 40 or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom - 40 >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
