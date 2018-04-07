# im confused about whats happening im just going to move
# things so everything is cleaner.
import pygame

BLUE = (50, 50, 255)

def makeGraph():
    pass
    for i in range()

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


# generate borders

def makeWalls(all_sprite_list): # (x, y, width, height)
    wall_list = pygame.sprite.Group()
    #borders
    wall = Wall(0,0, 10, 400)#Wall(0, 0, 10, 600) LEFT BORDER
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(10,0, 600, 10)#Wall(10, 0, 800, 10) TOP BORDER
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(590, 0, 10, 400)
    #RIGHT MOST WALL #wall = Wall(0, 590, 800, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(0, 390, 600, 10)
    #BOTTOM #wall = Wall(790, 0, 10, 600)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #upper left corner area
    wall = Wall(150, 0, 10, 80)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(100, 40, 150, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #top right corner
    wall = Wall(380, 50, 220, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #bottom left
    wall = Wall(160, 180, 10, 300)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #left middle
    wall = Wall(100, 130, 190, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(280, 90, 10, 120)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(210, 180, 30, 150)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(290, 200, 270, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(290, 310, 220, 50)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(350, 270, 10, 60)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(380, 100, 160, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(330, 10, 10, 150)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(380, 150, 400, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(450, 270, 170, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(40, 80, 30, 270)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(100, 180, 30, 170)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(280, 240, 130, 120)
    wall_list.add(wall)
    all_sprite_list.add(wall)





    return wall_list, all_sprite_list
