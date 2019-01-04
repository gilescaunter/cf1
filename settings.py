def init():
    # This is the area to work with (Set to 0 to start)
    global matrix
    matrix = [[0 for i in range(1500)] for i in range(1500)]
    global xOffset
    xOffset = 50
    global yOffset
    yOffset = 50
    global white
    white = (255, 255, 255)
    global black
    black = (0, 0, 0)
    global red
    red = (255, 0, 0)
