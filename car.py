import settings
import pygame

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.direction = 90
        self.currentSegment = 0
        self.destx = 0
        self.desty = 0
        self.route = []


    def placeCarOnGrid(self,x,y):
        #Do some magic and find a spot to place the car
        foundSpot = False
        while foundSpot == False:
            if settings.matrix[x][y] == 1:
                foundSpot = True
            else:
                x += 1
                y += 1

        #ok we have a start on the grid now convert to actual location
        self.x = x
        self.y = y
        print("Vehicle is now located")
        self.showDash()

    def setDirection(self, direction):
        self.direction = direction

    def setSpeed(self,speed):
        self.speed = speed

    def showDash(self):
        print("X=: "+ str(self.x) + " Y=: " + str(self.y) + " Speed=: " + str(self.speed) + " Direction=:" + str(self.direction))

    def showDashOnScreen(self,screen):
        matrix = settings.matrix
        font = pygame.font.Font(None, 26)
        dashText = "X=: "+ str(self.x) + " Y=: " + str(self.y) + " Speed=: " + str(self.speed) + " Direction=:" + str(self.direction) + "\n" \
                    + str(matrix[self.x-1][self.y-1]) + str(matrix[self.x][self.y-1]) + str(matrix[self.x+1][self.y-1]) + "\n" \
                    + str(matrix[self.x-1][self.y]) + str(matrix[self.x][self.y]) + str(matrix[self.x+1][self.y]) + "\n" \
                    + str(matrix[self.x-1][self.y+1]) + str(matrix[self.x][self.y+1]) + str(matrix[self.x+1][self.y+1]) + "\n" \
                    + "........................."



        text_surface = font.render(dashText, True, settings.red)
        screen.blit(text_surface, (0, 0))

    def carLeft(self):
        self.direction = self.direction - 90
        if self.direction < 0:
            self.direction = 270
        self.carForward()

    def carRight(self):
        self.direction += 90
        if self.direction > 270:
            self.direction = 0

    def carLeftRight(self):
        # Always go left for now... maze breaking
        self.carLeft()

    def carForward(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 90:
            self.x += 1
        elif self.direction == 270:
            self.x -= 1
        else:
            self.y += 1

    def carForwardLeft(self):
        # for now only go Forward
        self.carForward()

    def carForwardRight(self):
        self.carForward()

    def carForwardLeftRight(self):
        self.carForward()

    def displayMatrix(self):
        matrix = settings.matrix
        print("Matrix:")
        print(str(matrix[self.x-1][self.y-1]) +
              str(matrix[self.x][self.y-1]) +
              str(matrix[self.x+1][self.y-1]))
        print(str(matrix[self.x-1][self.y]) +
              str(matrix[self.x][self.y]) +
              str(matrix[self.x+1][self.y]))
        print(str(matrix[self.x-1][self.y+1]) +
              str(matrix[self.x][self.y+1]) +
              str(matrix[self.x+1][self.y+1]))
        print(".........................")

    def checkLeftRight(self):
        matrix = settings.matrix
        if (self.direction == 90):
            if ((matrix[self.x][self.y-1] ==1) and
                (matrix[self.x][self.y+1 == 1])):
                self.carLeftRight()
            elif (matrix[self.x][self.y-1] == 1):
                self.carLeft()
            elif (matrix[self.x][self.y+1] ==1):
                self.carRight()
            else:
                 self.carStop()
        elif (self.direction == 180):
            if ((matrix[self.x - 1][self.y] == 1) and
                    (matrix[self.x + 1][self.y == 1])):
                self.carLeftRight()
            elif (matrix[self.x + 1][self.y] == 1):
                self.carLeft()
            elif (matrix[self.x - 1][self.y] == 1):
                self.carRight()
            else:
                self.carStop()
        elif (self.direction == 270):
            if ((matrix[self.x][self.y - 1] == 1) and
                    (matrix[self.x][self.y + 1 == 1])):
                self.carLeftRight()
            elif (matrix[self.x][self.y + 1] == 1):
                self.carLeft()
            elif (matrix[self.x][self.y - 1] == 1):
                self.carRight()
            else:
                self.carStop()
        elif (self.direction == 0):
            if ((matrix[self.x][self.y - 1] == 1) and
                    (matrix[self.x - 1][self.y == 1])):
                self.carLeftRight()
            elif (matrix[self.x - 1][self.y] == 1):
                self.carLeft()
            elif (matrix[self.x + 1][self.y] == 1):
                self.carRight()
            else:
                self.carStop()
        else:
            print ("Error No Direction: " + str(self.direction))


    def movePlusX(self):
        matrix = settings.matrix
        self.displayMatrix()
        # There is no way forward so stop (or even reverse ... later)
        if (matrix[self.x+1][self.y] == 0
            and matrix[self.x+1][self.y - 1] ==0
            and matrix[self.x+1][self.y + 1] == 0):
            self.checkLeftRight()

        elif (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carLeft()

        elif (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carRight()

        elif (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carLeftRight()

        elif (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 0):
            self.carForward()

        elif (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carForwardLeft()

        elif (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardRight()

        elif (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardLeftRight()

    def movePlusY(self):
        matrix = settings.matrix
        self.displayMatrix()
        # There is no way forward so stop (or even reverse ... later)
        if (matrix[self.x][self.y + 1] == 0
            and matrix[self.x-1][self.y + 1] ==0
            and matrix[self.x+1][self.y + 1] == 0):
            self.checkLeftRight()

        elif (matrix[self.x + 1][self.y+1] == 1
                and matrix[self.x][self.y + 1] == 1
                and matrix[self.x - 1][self.y + 1] == 0):
            self.carLeft()

        elif (matrix[self.x][self.y + 1] == 0
                and matrix[self.x + 1][self.y + 1] == 0
                and matrix[self.x - 1][self.y + 1] == 1):
            self.carRight()

        elif (matrix[self.x][self.y + 1] == 0
                and matrix[self.x - 1][self.y + 1] == 1
                and matrix[self.x + 1][self.y + 1] == 1):
            self.carLeftRight()

        elif (matrix[self.x][self.y + 1] == 1
                and matrix[self.x - 1][self.y + 1] == 0
                and matrix[self.x + 1][self.y + 1] == 0):
            self.carForward()

        elif (matrix[self.x][self.y + 1] == 1
                and matrix[self.x + 1][self.y + 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carForwardLeft()

        elif (matrix[self.x][self.y + 1] == 1
                and matrix[self.x + 1][self.y + 1] == 0
                and matrix[self.x - 1][self.y + 1] == 1):
            self.carForwardRight()

        elif (matrix[self.x + 1][self.y + 1] == 1
                and matrix[self.x - 1][self.y + 1] == 1
                and matrix[self.x + 1][self.y + 1] == 1):
            self.carForwardLeftRight()


    def moveMinusY(self):
        # 000
        # 010 Must Stop

        # 000
        # 011 Must Move Right

        # 000
        # 110 Must Move Left

        # 000
        # 111 Must Move Left or Right

        # 010
        # 110 Can move Left

        # 010
        # 011 Can move Right

        # 010
        # 111 Can Move Left or right



        matrix = settings.matrix
        self.displayMatrix()
        # There is no way forward so stop (or even reverse ... later)
        if (matrix[self.x][self.y - 1] == 0
            and matrix[self.x-1][self.y - 1] ==0
            and matrix[self.x+1][self.y - 1] == 0):
            self.checkLeftRight()

        elif (matrix[self.x][self.y] == 0
                and matrix[self.x - 1][self.y - 1] == 1
                and matrix[self.x + 1][self.y + 1] == 0):
            self.carLeft()

        elif (matrix[self.x][self.y] == 0
                and matrix[self.x - 1][self.y - 1] == 0
                and matrix[self.x + 1][self.y + 1] == 1):
            self.carRight()

        elif (matrix[self.x][self.y - 1] == 0
                and matrix[self.x - 1][self.y - 1] == 1
                and matrix[self.x + 1][self.y - 1] == 1):
            self.carLeftRight()

        elif (matrix[self.x][self.y - 1] == 1
                and matrix[self.x - 1][self.y - 1] == 0
                and matrix[self.x + 1][self.y - 1] == 0):
            self.carForward()

        elif (matrix[self.x][self.y - 1] == 1
                and matrix[self.x - 1][self.y - 1] == 1
                and matrix[self.x + 1][self.y - 1] == 0):
            self.carForwardLeft()

        elif (matrix[self.x][self.y - 1] == 1
                and matrix[self.x - 1][self.y - 1] == 0
                and matrix[self.x + 1][self.y - 1] == 1):
            self.carForwardRight()

        elif (matrix[self.x][self.y - 1] == 1
                and matrix[self.x - 1][self.y - 1] == 1
                and matrix[self.x + 1][self.y - 1] == 1):
            self.carForwardLeftRight()


    def moveMinusX(self):
        matrix = settings.matrix
        self.displayMatrix()
        # There is no way forward so stop (or even reverse ... later)
        if (matrix[self.x - 1][self.y] == 0
            and matrix[self.x - 1][self.y - 1] ==0
            and matrix[self.x - 1][self.y + 1] == 0):
            self.checkLeftRight()

        elif (matrix[self.x - 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carLeft()

        elif (matrix[self.x - 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carRight()

        elif (matrix[self.x - 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carLeftRight()

        elif (matrix[self.x - 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 0):
            self.carForward()

        elif (matrix[self.x - 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carForwardLeft()

        elif (matrix[self.x - 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardRight()

        elif (matrix[self.x - 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardLeftRight()

    def getDirections(self):
        if self.direction == 0:
            forward = (0,-1)
            left = (-1,-1)
            right = (1, -1)
            directions = {"forward": forward, "left":left, "right":right}
        elif self.direction == 90:
            forward = (1, 0)
            left = (1, -1)
            right = (1, 1)
            directions = {"forward": forward, "left": left, "right": right}
        elif self.direction == 180:
            forward = (0, 1)
            left = (1, 1)
            right = (-1, 1)
            directions = {"forward": forward, "left": left, "right": right}
        else self.direction == 270:
            forward = (-1, 0)
            left = (-1, 1)
            right = (-1, -1)
            directions = {"forward": forward, "left": left, "right": right}
        return directions

    def getOptions(self,directions):
        options = []
        matrix = settings.matrix
        x,y = directions["forward"]
        if matrix[self.x + x][self.y + y] == 1:
            options.add("forward")
        x,y = directions["left"]
        if matrix[self.x + x][self.y + y] == 1:
            options.add("left")
        x,y = directions["right"]
        if matrix[self.x + x][self.y + y] == 1:
            options.add("right")
        return options

    def move(self):
        directions = self.getDirections()
        options = self.getOptions(directions)



    def move(self):
        if self.direction == 90:
            self.movePlusX()
        elif self.direction == 0:
            self.movePlusY()
        elif self.direction == 180:
            self.moveMinusY()
        elif self.direction == 270:
            self.moveMinusX()
        else:
            print("not implemented")

    def routeAdd(self, routeSegment):
        self.route.append(routeSegment)

    def carStart(self):
        self.carRunning = True

    def carStop(self):
        self.carRunning = False
        self.speed = 0
        print("Journey Stopped")

