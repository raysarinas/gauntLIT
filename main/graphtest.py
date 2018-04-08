def generate_graph(screenwidth, screenheight, walls):
    xrange = (screenwidth - 10) // 25
    yrange = (screenheight - 10) // 25
    print(xrange, yrange)
    print(walls)
    vertices = []

    for i in range(xrange):
        for j in range(yrange):
            vertices.append([25 * i, 25 * j])

    print(vertices)
    print(len(vertices))




#generate_graph(600, 400)
