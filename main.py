import car
import map
import pygame
import sys

pygame.init()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

segments = [(10,10),(10,500),(500,500),(500,10)]

screen = pygame.display.set_mode((1500,1200))
clock = pygame.time.Clock()

screen.fill(white)

map = map.Map()
map.drawLines(screen)

pygame.display.update()

#Create a Car
car = car.Car(10,10,10, 0)

#Plot a route for car
for i in segments:
    car.routeAdd(i)

#Put car on first part of the route
car.carStart()
pygame.draw.line(screen,red,(car.x,car.y),(car.x,car.y),3)

#show where we are
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

    screen.fill(white)
    map.drawLines(screen)
    pygame.draw.circle(screen, red, (car.x, car.y), 3, 3)

    pygame.display.update()

    msElapsed = clock.tick(10)




