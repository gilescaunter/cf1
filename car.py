import settings
import pygame
import random

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 10
        self.direction = 0
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

    def changeDirection(self,direction):
        if direction == 'left':
            self.direction -= 90
            if self.direction < 0:
                self.direction = 270
        else:
            self.direction += 90
            if self.direction > 270:
                self.direction = 0

    def carLeft(self, directions):
        x,y = directions['left']
        self.x += x
        self.y += y
        self.changeDirection('left')

    def carRight(self,directions):
        x,y = directions['right']
        self.x += x
        self.y += y
        self.changeDirection('right')

    def carLeftRight(self,directions):
        # Always go left for now... maze breaking
        if random.randint(1,3) == 1:
            self.carLeft(directions)
        else:
            self.carRight(directions)

    def carForward(self, directions):
        x,y = directions['forward']
        self.x += x
        self.y += y

    def carForwardLeft(self,directions):
        # for now only go Left (Solve the Maze)
        if random.randint(1,3) == 1:
            self.carLeft(directions)
        else:
            self.carForward(directions)

    # If we have no further forwards we must force right left or stop
    def nextForward(self,directions):
        matrix = settings.matrix
        x,y = directions['forward']
        return matrix[self.x + x + x][self.y + y + y]


    def carForwardRight(self, directions):
        if random.randint(1,3) == 1:
            if self.nextForward(directions) != 0:
                self.carForward(directions)
            else:
                self.carRight(directions)
        else:
                self.carRight(directions)

    def carForwardLeftRight(self, directions):
        if random.randint(1,3) == 1:
            if self.nextForward(directions) != 0:
                self.carForward(directions)
            else:
                self.carLeft(directions)
        else:
            if random.randint(1,3) == 1:
                self.carLeft(directions)
            else:
                self.carRight(directions)

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
        elif self.direction == 270:
            forward = (-1, 0)
            left = (-1, 1)
            right = (-1, -1)
            directions = {"forward": forward, "left": left, "right": right}
        return directions

    def getOptions(self,directions):
        options = []
        self.displayMatrix()
        matrix = settings.matrix
        x,y = directions["forward"]
        if matrix[self.x + x][self.y + y] == 1:
            options.append("forward")
        x,y = directions["left"]
        if matrix[self.x + x][self.y + y] == 1:
            options.append("left")
        x,y = directions["right"]
        if matrix[self.x + x][self.y + y] == 1:
            options.append("right")
        return options

    def move(self):
        directions = self.getDirections()
        options = self.getOptions(directions)
        if 'left' in options and 'right' in options and 'forward' in options:
            self.carForwardLeftRight(directions)
        elif 'left' in options and 'forward' in options:
            self.carForwardLeft(directions)
        elif 'right' in options and 'forward' in options:
            self.carForwardRight(directions)
        elif 'left' in options and 'right' in options:
            self.carLeftRight(directions)
        elif 'left' in options:
            self.carLeft(directions)
        elif 'right' in options:
            self.carRight(directions)
        elif 'forward' in options:
            self.carForward(directions)
        else:
            self.carStop()

    def routeAdd(self, routeSegment):
        self.route.append(routeSegment)

    def carStart(self):
        self.carRunning = True

    def carStop(self):
        self.carRunning = False
        self.speed = 0
        print("Journey Stopped")

