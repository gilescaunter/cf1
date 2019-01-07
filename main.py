import car
import map
import pygame
import sys
import settings


settings.init()
pygame.init()


segments = [(10,10),(10,500),(500,500),(500,10)]

screen = pygame.display.set_mode((1500,1200))
clock = pygame.time.Clock()

screen.fill(settings.white)

map = map.Map()
map.drawLines(screen,settings.xOffset,settings.yOffset)

pygame.display.update()

#Create a Car
car = car.Car()
car.placeCarOnGrid(500,500)
car.setDirection(90)
car.setSpeed(10)

#Put car on first part of the route
car.carStart()
pygame.draw.line(screen,settings.red,(car.x+settings.xOffset,car.y+settings.yOffset),(car.x+settings.xOffset,car.y+settings.yOffset),3)

#show where we are.
car.showDash()

#move car

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if car.carRunning == True:
        car.move()
        car.showDash()
        car.showDashOnScreen(screen)
    screen.fill(settings.white)
    map.drawLines(screen,settings.xOffset,settings.yOffset)
    pygame.draw.circle(screen, settings.red, (car.x+settings.xOffset, car.y+settings.yOffset), 3, 3)

    pygame.display.update()

    msElapsed = clock.tick(10)




