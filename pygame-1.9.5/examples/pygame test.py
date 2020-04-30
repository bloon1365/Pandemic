import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Window
gameDisplay = pygame.display.set_mode((display_width,display_height))

#Name
pygame.display.set_caption('Cars')

#Clock
clock = pygame.time.Clock()

carImg = pygame.image.load("car.png")

def car (x,y):
	gameDisplay.blit(carImg, (x,y))

	x = (display_width * 0.45)
	y = (display_height * 0.8)

#Vars
crashed = False

print("wack")


while not crashed:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()