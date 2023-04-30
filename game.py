import pygame
from sys import exit

# with starting of every game, you have to start with pygame init
pygame.init()
screen = pygame.display.set_mode((800,400)) # black
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/FFFFORWA.TTF', 50)


sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My game', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail.png')
snail_x_pos = 600

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface, (0,300))
	screen.blit(text_surface, (300, 50))
	snail_x_pos -= 1
	if snail_x_pos < -100: snail_x_pos = 800
	screen.blit(snail_surface, (snail_x_pos,270))

	pygame.display.update()	
	clock.tick(60)



# mango

