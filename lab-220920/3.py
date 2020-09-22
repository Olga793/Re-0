import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 100, 0)
circle(screen, (255, 255, 255), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (240, 170), 20, 0)
circle(screen, (255, 0, 0), (160, 170), 15, 0)
circle(screen, (0, 0, 0), (240, 170), 20, 1)
circle(screen, (0, 0, 0), (160, 170), 15, 1)
circle(screen, (0, 0, 0), (240, 170), 6, 0)
circle(screen, (0, 0, 0), (160, 170), 6, 0)
line(screen, (0, 0, 0), (220, 155), (270, 140), 8)
line(screen, (0, 0, 0), (180, 160), (130, 145), 8)
line(screen, (0, 0, 0), (155, 250), (245, 250), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (pygame.time.get_ticks() > 5000):
            finished = True

pygame.quit()
