class Car:
    def __init__(self,x,y,speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.currentSegment = 0
        self.destx = x
        self.desty = y
        self.route = []


    def showDash(self):
        print("X=: "+ str(self.x) + " Y=: " + str(self.y) + " Speed=: " + str(self.speed) + " Direction=:" + str(self.direction))

    def movePlusX(self):
        if self.x + self.speed <= self.destx:
            self.x += self.speed
        else:
            #add here later the number of spaces to move on next segment so flow is continious
            self.nextSegment()

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