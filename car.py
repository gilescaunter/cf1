import settings

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

    def setDirection(self, direction):
        self.direction = direction

    def setSpeed(self,speed):
        self.speed = speed

    def showDash(self):
        print("X=: "+ str(self.x) + " Y=: " + str(self.y) + " Speed=: " + str(self.speed) + " Direction=:" + str(self.direction))


    def carLeft(self):
        self.direction = self.direction - 90
        if self.direction < 0:
            self.direction = 270
        self.y -= 1

    def carRight(self):
        self.direction += 90
        if self.direction > 270:
            self.direction = 0

    def carLeftRight(self):
        # Always go left for now... maze breaking
        self.carLeft()

    def carForward(self):
        self.x += 1

    def carForwardLeft(self):
        # for now only go Forward
        self.carForward()

    def carForwardRight(self):
        self.carForward()

    def carForwardLeftRight(self):
        self.carForward()

    def movePlusX(self):
        matrix = settings.matrix
        # There is no way forward so stop (or even reverse ... later)
        if (matrix[self.x+1][self.y] == 0
            and matrix[self.x+1][self.y - 1] ==0
            and matrix[self.x+1][self.y + 1] == 0):
            self.carStop()

        if (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carLeft()

        if (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carRight()

        if (matrix[self.x + 1][self.y] == 0
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carLeftRight()

        if (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 0):
            self.carForward()

        if (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 0):
            self.carForwardLeft()

        if (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 0
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardRight()

        if (matrix[self.x + 1][self.y] == 1
                and matrix[self.x][self.y - 1] == 1
                and matrix[self.x][self.y + 1] == 1):
            self.carForwardLeftRight()

    def movePlusY(self):
        if self.y + self.speed <= self.desty:
            self.y += self.speed
        else:
            #add here later the number of spaces to move on next segment so flow is continious
            self.nextSegment()

    def moveMinusY(self):
        if self.y - self.speed >= self.desty:
            self.y -= self.speed
        else:
            #add here later the number of spaces to move on next segment so flow is continious
            self.nextSegment()

    def moveMinusX(self):
        if self.x - self.speed >= self.destx:
            self.x -= self.speed
        else:
            #add here later the number of spaces to move on next segment so flow is continious
            self.nextSegment()





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
        self.x, self.y = self.route[0]
        self.destx, self.desty = self.route[1]
        self.currentSegment = 1
        self.carRunning = True

    def carStop(self):
        self.carRunning = False
        self.speed = 0
        print("Journey Stopped")

    def nextSegment(self):
        #First see if we have any more segments
        if self.currentSegment == len(self.route) - 1:
            self.carStop()
        else:
            self.x,self.y = self.route[self.currentSegment]
            self.currentSegment += 1
            self.destx,self.desty = self.route[self.currentSegment]

            #See if we need a new direction and change it
            self.checkDirection()

    def checkDirection(self):
        if self.destx > self.x:
            self.direction = 90
        elif self.destx < self.x:
            self.direction = 270
        elif self.desty > self.y:
            self.direction = 0
        else:
            self.direction = 180