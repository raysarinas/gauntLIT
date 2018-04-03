# im confused about whats happening im just going to move
# things so everything is cleaner.
import pygame
BLUE = (128, 0, 128)#(50, 50, 255)

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
    wall = Wall(350, 0, 10, 130)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(70, 120, 290, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #two top middle area
    wall = Wall(500, 0, 10, 70)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(580, 0, 10, 70)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #bottom left corner area
    wall = Wall(70, 500, 250, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(320, 500, 10, 100)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #middle area
    wall = Wall(150, 280, 10, 100)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(250, 280, 10, 100)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(150, 380, 110, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #right bottom area
    wall = Wall(700, 300, 10, 400)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #top right area
    wall = Wall(600, 200, 300, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    #right in the middle(sprial)
    wall = Wall(600, 200, 10, 300)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(410, 500, 200, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(410, 300, 10, 200)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(410, 300, 100, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    wall = Wall(510, 400, 100, 10)
    wall_list.add(wall)
    all_sprite_list.add(wall)

    return wall_list, all_sprite_list
