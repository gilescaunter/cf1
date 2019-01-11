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
#car.placeCarOnGrid(550,327)
car.placeCarOnGrid(925,2)
car.setDirection(0)
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
    screen.fill(settings.white)
    map.drawLines(screen,settings.xOffset,settings.yOffset)
    pygame.draw.circle(screen, settings.red, (car.x+settings.xOffset, car.y+settings.yOffset), 3, 3)

    matrix = settings.matrix
    font = pygame.font.Font(None, 26)
    dashText = "X=: " + str(car.x) + " Y=: " + str(car.y) + " Speed=: " + str(car.speed) + " Direction=:" + str(
        car.direction) + "\n" \
               + str(matrix[car.x - 1][car.y - 1]) + str(matrix[car.x][car.y - 1]) + str(
        matrix[car.x + 1][car.y - 1]) + "\n" \
               + str(matrix[car.x - 1][car.y]) + str(matrix[car.x][car.y]) + str(matrix[car.x + 1][car.y]) + "\n" \
               + str(matrix[car.x - 1][car.y + 1]) + str(matrix[car.x][car.y + 1]) + str(
        matrix[car.x + 1][car.y + 1]) + "\n" \
               + "........................."

    largeText = pygame.font.Font('freesansbold.ttf', 12)
    TextSurf = largeText.render(dashText, True, settings.black)
    TextRect = TextSurf.get_rect()
    TextRect.center = (500, 500)
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    msElapsed = clock.tick(20)


    def message_box(text):
        pos = 560  # depends on message box location
        pygame.draw.rect(root, (0, 0, 0), (100, 550, 800, 200))  # rectangle position varies
        for x in range(len(text)):
            rendered = sys_font.render(text[x], 0, (255, 255, 255))
            root.blit(rendered, (110, pos))
            pos += 30  # moves the following line down 30 pixels






