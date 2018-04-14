import pygame

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """

    def __init__(self, wallrect):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()

        # Make a wall (using wallrect list to get it's size)
        self.sprite = pygame.image.load('images/bricks.png')
        self.width = wallrect[2]
        self.height = wallrect[3]
        self.image = pygame.Surface([self.width, self.height])

        # top-left corner is where we initiate to draw the wall
        self.rect = self.image.get_rect()
        self.image.blit(self.sprite, self.rect)
        self.rect.x, self.rect.y = wallrect[0], wallrect[1]

def generate_walls(all_sprite_list):
    """
    Generates maze wall/border sprites onto the screen by parsing a text file.
    Returns a 'group' of sprites representing the maze borders/walls, an
    updated list of all the sprites used in the game, and a list of the walls
    which each entry representing a rectangle.
    """
    walls = []

    with open('../map.txt', 'r') as filename:
        # parse wall/border starting coordinates and size and store appropriately.
        for line in filename:
            row = line.strip().split(",")

            topleftx = int(row[0])
            toplefty = int(row[1])
            width = int(row[2])
            height = int(row[3])
            wallrect = [topleftx, toplefty, width, height]
            walls.append(wallrect)

    # make a group of pygame sprites which will be a list of the wall sprites
    wall_list = pygame.sprite.Group()

    # create an instance of a wall and append each wall to both the list of
    # wall sprites and the entire list of sprites utilized in the game
    for i in range(len(walls)):
        wall = Wall(walls[i])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    return wall_list, all_sprite_list, walls
