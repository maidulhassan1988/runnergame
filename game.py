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
text_surface = test_font.render('My game', False, 'black')

snail_surface = pygame.image.load('graphics/snail/snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics/player/player1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	screen.blit(sky_surface,(0,0))
	screen.blit(ground_surface, (0,300))
	screen.blit(text_surface, (300, 50))


	snail_rect.x -=4
	if snail_rect.right <=0: snail_rect.left = 800
	screen.blit(snail_surface, snail_rect)
	player_rect.left +=1
	screen.blit(player_surface, player_rect)

	if player_rect.colliderect(snail_rect):
		print('collision')

	pygame.display.update()	
	clock.tick(60)
