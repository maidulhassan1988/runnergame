import pygame
from sys import exit

# with starting of every game, you have to start with pygame init
pygame.init()
screen = pygame.display.set_mode((800,400)) # black
pygame.display.set_caption('Runner Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/FFFFORWA.TTF', 50)


sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('snail game', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail.png').convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load('graphics/player/player1.png').convert_alpha()
player_rect = player_surface.get_rect()

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
	screen.blit(player_surface, (80,200))

	pygame.display.update()	
	clock.tick(60)
