import sys
import pygame
from settings import *
from player import Player
from car import Car
from all_sprites import AllSprites

# basic setup
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')
clock = pygame.time.Clock()

# groups
all_sprites = AllSprites()

# sprites
player = Player((500, 400), all_sprites)
car = Car((700, 100), all_sprites)

# game loop
while True:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# delta time
	dt = clock.tick() / 1000

	# draw a bg
	display_surface.fill('black')

	# update
	all_sprites.update(dt)

	# draw
	all_sprites.customize_draw(display_surface, ((player.rect.centerx - WINDOW_WIDTH / 2, player.rect.centery - WINDOW_HEIGHT / 2)))
	print(player.rect.centerx)
	print(player.rect.centerx - WINDOW_WIDTH / 2)

	# update the display surface
	pygame.display.update()
