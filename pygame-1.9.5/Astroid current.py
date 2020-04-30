import pygame
import math
import random

pygame.init()

display_width = 1600
display_height = 900

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('ship')

clock = pygame.time.Clock()

ship = pygame.image.load('ship.png')
shipfire = pygame.image.load('shipfire.png')
astroidimg50 = pygame.image.load('astroid50.png')
astroidimg100 = pygame.image.load('astroid100.png')
astroidimg200 = pygame.image.load('astroid200.png')

top_rect = pygame.Rect(0, 0, display_width, 10)
bot_rect = pygame.Rect(0, display_height, display_width, -10)
left_rect = pygame.Rect(0, 0, 10, display_height)
right_rect = pygame.Rect(display_width, 0, -10, display_height)

bounding_box = [top_rect, bot_rect, left_rect, right_rect]

image_rect = ship.get_rect()

crashed = False

Speed = 0
Rate_of_Rotation = 0
Rotation = 0
S1 = 0
R1 = 0
S2 = 0
R2 = 0
x_speed = 750
y_speed = 500
astroid_rect1 = astroidimg50.get_rect()
astroid_rect1.x += x_speed
astroid_rect1.y += y_speed

fire = False

time = 180

def speed(time):
	diff = round(10 * (time / 180))
	return random.randrange(4, 7)

x1 = 500
y1 = 500
astroid_speed1 = 3
astroid_angle1 = random.randrange(0, 360)

def astroid(astroid_img, astroid_rect1, astroid_speed1, astroid_angle1, x_speed, y_speed, x1, y1, top_rect , bot_rect, left_rect , right_rect):
	if astroid_rect1.colliderect(top_rect):
		if astroid_angle1 > 90 and astroid_angle1 < 270:
			astroid_angle1 = ((90 - astroid_angle1) * 2) + astroid_angle1
	elif astroid_rect1.colliderect(bot_rect):
		if astroid_angle1 < 90 and astroid_angle1 > 0 or astroid_angle1 > 180 and astroid_angle1 > 270:
			astroid_angle1 = ((90 - astroid_angle1) * 2) + astroid_angle1
	elif astroid_rect1.colliderect(left_rect):
		if astroid_angle1 > 0 and astroid_angle1 > 180:
			astroid_angle1 = ((180 - astroid_angle1) * 2) + astroid_angle1
	elif astroid_rect1.colliderect(right_rect):
		if astroid_angle1 > 0 and astroid_angle1 < 180:
			astroid_angle1 = ((180 - astroid_angle1) * 2) + astroid_angle1

	if astroid_angle1 > 360:
		astroid_angle1 = astroid_angle1 - 360
	if astroid_angle1 < 0:
		astroid_angle1 = astroid_angle1 + 360
	print(astroid_angle1)

	x_speed = math.sin(math.radians(astroid_angle1)) * astroid_speed1
	y_speed = math.cos(math.radians(astroid_angle1)) * astroid_speed1

	astroid_rect1.x += x_speed
	astroid_rect1.y += y_speed

	astroidimg50.set_colorkey([255,255,255])
	gameDisplay.blit(astroid_img, astroid_rect1)

	

while not crashed:

	astroid_speed1 = (time / 250) + 4

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

		if event.type == pygame.KEYUP: 
			if event.key == pygame.K_w: 
				S1 = 0 
			if event.key == pygame.K_s: 
				S2 = 0 
			if event.key == pygame.K_a: 
				R1 = 0 
			if event.key == pygame.K_d: 
				R2 = 0
		if event.type == pygame.KEYDOWN: 
			if event.key == pygame.K_w: 
				S1 = -10
			if event.key == pygame.K_s: 
				S2 = 10
			if event.key == pygame.K_a: 
				R1 = 0.1
			if event.key == pygame.K_d: 
				R2 = -0.1

	Speed = S1 + S2
	Rate_of_Rotation = R1 + R2

	Rotation += Rate_of_Rotation

	gameDisplay.fill(white)

	if Speed > 0 or Speed < 0:
		ship_image = shipfire
	else:
		ship_image = ship


	x_speed = math.sin(Rotation) * Speed
	y_speed = math.cos(Rotation) * Speed


	ship_image = pygame.transform.rotate(ship_image, math.degrees(Rotation))

	image_rect = ship_image.get_rect(center=image_rect.center)

	image_rect.x += x_speed
	image_rect.y += y_speed

	ship_rect = ship_image.get_rect()
	gameDisplay.blit(ship_image, image_rect)

	astroid(astroidimg50, astroid_rect1, astroid_speed1, astroid_angle1, x_speed, y_speed, x1, y1, top_rect , bot_rect, left_rect , right_rect)

	#print(time)

	time += 1

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()