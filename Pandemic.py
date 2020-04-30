import pygame
import os
import pickle as p
import random

pygame.init()

display_width = 1920
display_height = 1080

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pandemic')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

dudes = 10000
radius = 10
infect = 0.3
movement = 7

def rendermap():
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, (900, 100, 920, 880), 3)

def movedude(dude):
    xin = random.randrange(-movement, movement)
    yin = random.randrange(-movement, movement)

    if dude[0] + xin > 1820:
        dude = (dude[0] - movement*3, dude[1], dude[2])
    elif dude[0] + xin < 900:
        dude = (dude[0] + movement*3, dude[1], dude[2])
    else:
        dude = (dude[0] + xin + 0.5, dude[1], dude[2])

    if dude[1] + yin > 980:
        dude = (dude[0], dude[1] - movement*3, dude[2])
    elif dude[1] + yin < 100:
        dude = (dude[0], dude[1] + movement*3, dude[2])
    else:
        dude = (dude[0], dude[1] + yin + 0.5, dude[2])

    return dude

def within(dude):
    for dude2 in dudelist:
        if dude2[2] is not True:
            continue
        if abs(dude2[0] - dude[0]) <= radius and abs(dude2[1] - dude[1]) <= radius:
            return True
            if random.random() < 0.1:
                return True
    return False

dudelist = []
index = 0
while index <= dudes:
    x = random.randrange(900, 1820)
    y = random.randrange(100, 980)
    infect = False
    if index < 25:
        infect = True
    dudelist.append((x, y, infect))
    index += 1

font = pygame.font.SysFont("comicsansms", 72)

current = []

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            pygame.quit()
            outfile = open('graph', 'wb')
            p.dump(current, outfile)
            outfile.close()

            quit()

    rendermap()
    index = 0
    for dude in dudelist:
        if dude[2] == True:
            pygame.draw.circle(gameDisplay, red, (round(dude[0]), round(dude[1])), 3)
        if dude[2] == False:
            pygame.draw.circle(gameDisplay, black, (round(dude[0]), round(dude[1])), 3)

        dude = movedude(dude)
        if dude[2] == False:
            dude = (dude[0], dude[1], within(dude))
        dudelist[index] = dude

        index += 1

    infected = 0
    healthy = dudes
    for dude in dudelist:
        if dude[2] == True:
            infected += 1
            healthy -= 1

    text = font.render(str(infected), True, red)
    text2 = font.render(str(healthy), True, black)
    gameDisplay.blit(text, (100, 100))
    gameDisplay.blit(text2, (100, 200))
    current.append(infected)


    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()