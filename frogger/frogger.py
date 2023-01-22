import sys
from random import choice, randint
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

# timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# game loop
while True:

	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == car_timer:
			random_pos = choice(CAR_START_POSITIONS)
			if random_pos not in pos_list:
				pos_list.append(random_pos)
				pos = (random_pos[0], random_pos[1] + randint(-8, 8))
				Car(pos, all_sprites)
			if len(pos_list) > 5:
				del pos_list[0]

	# delta time
	dt = clock.tick() / 1000

	# update
	all_sprites.update(dt)

	# draw
	all_sprites.customize_draw(display_surface, ((player.rect.centerx - WINDOW_WIDTH / 2, player.rect.centery - WINDOW_HEIGHT / 2)))

	# update the display surface
	pygame.display.update()
