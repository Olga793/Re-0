import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))

rect(screen, (0, 255, 255), (0, 0, 794, 623))
rect(screen, (255, 255, 255), (0, 623, 794, 500))
line(screen, (0, 0, 0), (0, 623), (794, 623), 1)
line(screen, pygame.Color(255, 255, 192), (200, 250), (700, 250), 20)
line(screen, pygame.Color(255, 255, 192), (450, 0), (450, 500), 20)
circle(screen, pygame.Color(255, 255, 128), (450, 250), 25, 0)
circle(screen, pygame.Color(255, 255, 128), (450, 250), 250, 20)
ellipse(screen, (0, 0, 0), rect(0, 500, 200, 500), 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.time.get_ticks() > 5000):
            finished = True

pygame.quit()
