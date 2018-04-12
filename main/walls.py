# im confused about whats happening im just going to move
# things so everything is cleaner.
import pygame

BLUE = (117, 122, 163)

class Wall1(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, wallrect):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a blue wall, of the size specified in the parameters
        self.sprite = pygame.image.load('images/bricks.png')
        self.width = wallrect[2]
        self.height = wallrect[3]
        self.image = pygame.Surface([self.width, self.height])
        #self.image.fill(BLUE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.image.blit(self.sprite, self.rect)
        self.rect.y = wallrect[1]
        self.rect.x = wallrect[0]

        # # Make our top-left corner the passed-in location.
        # self.rect = self.image.get_rect()
        self.rect.y = wallrect[1]
        self.rect.x = wallrect[0]

# GENERATE BORDERS MORE EFFICIENTLY:
def generate_walls(all_sprite_list):
    walls = []

    with open('../map.txt', 'r') as filename:
        for line in filename:
            row = line.strip().split(",")

            topleftx = int(row[0])
            toplefty = int(row[1])
            width = int(row[2])
            height = int(row[3])
            wallrect = [topleftx, toplefty, width, height]
            walls.append(wallrect)

    wall_list = pygame.sprite.Group()

    for i in range(len(walls)):
        wall = Wall1(walls[i])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    return wall_list, all_sprite_list, walls
