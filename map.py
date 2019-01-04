import pygame

class Map:


        def __init__(self):
            self.grid = []
            self.lines = [
                [(0, 0), (1175, 0)],
                [(1175, 0), (1175, 975)],
                [(1175, 975), (0, 975)],
                [(0, 975), (0, 0)],
                [(25, 25), (275, 25)],
                [(275, 25), (275, 850)],
                [(25, 750), (300, 750)],
                [(25, 850), (275, 850)],
                [(25, 25), (25, 850)],
                [(150, 25), (150, 750)],
                [(25, 425), (275, 425)],
                [(300, 0), (300, 875)],
                [(300, 475), (550, 475)],
                [(0, 875), (1175, 875)],
                [(550, 325), (900, 325)],
                [(550, 325), (550, 700)],
                [(900, 325), (900, 700)],
                [(550, 700), (900, 700)],
                [(900, 550), (1175, 550)],
                [(700, 225), (700, 325)],
                [(700, 225), (1025, 225)],
                [(925, 0), (925, 225)],
                [(1025, 75), (1150, 75)],
                [(1025, 75), (1025, 300)],
                [(1025, 300), (1150, 300)],
                [(1150, 300), (1150, 75)],
                [(1150, 275), (1175, 275)]]
            self.black = (0,0,0)
            self.matrix = [[0 for i in xrange(1500)] for i in xrange(1500)]
            self.buildGrid()

        def buildGrid(self):
            for i in self.lines:
                lineStart = i[0]
                x1,y1 = lineStart
                lineEnd = i[1]
                x2,y2 = lineEnd

                # make sure we count the right way
                stepx = 1
                if x2 < x1:
                    stepx = -1
                stepy = 1
                if y2 < y1:
                    stepy = -1

                # fill in a simple path here (later this will include complex items in the path)
                for i in range(x1,x2, stepx):
                    for j in range(y1,y2,stepy):
                        self.grid[i][j] = 1



        def drawLines(self, screen):

            xOffset = 50
            yOffset = 50

            for i in self.lines:
                lineStart = i[0]
                x1,y1 = lineStart
                lineEnd = i[1]
                x2,y2 = lineEnd
                pygame.draw.line(screen,self.black,(x1+xOffset, y1+yOffset),(x2+xOffset, y2+yOffset),5)


