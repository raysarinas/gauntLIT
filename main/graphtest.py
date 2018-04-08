# GENERATE BORDERS MORE EFFICIENTLY:
def generate_walls():#all_sprite_list):
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

    for i in range(len(walls)):
        print(walls[i])



def generate_graph(screenwidth, screenheight, walls):
    xrange = (screenwidth - 10) // 25
    yrange = (screenheight - 10) // 25

    for i in range(xrange):
        pass


generate_walls()
#generate_graph(600, 400)
