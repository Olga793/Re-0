# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:01:14 2020

@author: Ольга
"""

import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

CAT_COLOR = (250, 155, 12)
BLACK = (0, 0, 0)

def background():
    polygon(screen, (255, 255, 255), [(150,20), (350,20), (350,200), (150,200)])
    polygon(screen, (42, 221, 245), [(160,25), (250,25), (250,90), (160,90)])
    polygon(screen, (42, 221, 245), [(255,25), (340,25), (340,90), (255,90)])
    polygon(screen, (42, 221, 245), [(160,100), (250,100), (250,195), (160,195)])
    polygon(screen, (42, 221, 245), [(255,100), (340,100), (340,195), (255,195)])
    rect(screen, (105, 65, 5), (0, 200, 400, 400))
    
def cat():
    circle(screen, CAT_COLOR, (340, 240), 30)
    circle(screen, BLACK, (340, 240), 30, 1)
    ellipse(screen, CAT_COLOR, (100, 200, 250, 100))
    ellipse(screen, BLACK, (100, 200, 250, 100), 1)
    circle(screen, CAT_COLOR, (120, 200), 50)
    circle(screen, BLACK, (120, 200), 50, 1)
    circle(screen, CAT_COLOR, (280, 270), 40)
    circle(screen, BLACK, (280, 270), 40, 1)
    ellipse(screen, CAT_COLOR, (340, 230, 45, 100))
    ellipse(screen, BLACK, (340, 230, 45, 100), 1)
    ellipse(screen, CAT_COLOR, (300, 260, 35, 90))
    ellipse(screen, BLACK, (300, 260, 35, 90), 1)
    ellipse(screen, CAT_COLOR, (80, 240, 30, 40))
    ellipse(screen, BLACK, (80, 240, 30, 40), 1)
    ellipse(screen, CAT_COLOR, (100, 260, 70, 40))
    ellipse(screen, BLACK, (100, 260, 70, 40), 1)
    circle(screen, CAT_COLOR, (340, 240), 30)
    circle(screen, BLACK, (340, 240), 30, 1)
    ellipse(screen, CAT_COLOR, (100, 200, 250, 100))
    ellipse(screen, BLACK, (100, 200, 250, 100), 1)
    circle(screen, CAT_COLOR, (120, 200), 50)
    circle(screen, BLACK, (120, 200), 50, 1)
    circle(screen, CAT_COLOR, (280, 270), 40)
    circle(screen, BLACK, (280, 270), 40, 1)
    ellipse(screen, CAT_COLOR, (340, 230, 45, 100))
    ellipse(screen, BLACK, (340, 230, 45, 100), 1)
    ellipse(screen, CAT_COLOR, (300, 260, 35, 90))
    ellipse(screen, BLACK, (300, 260, 35, 90), 1)
    ellipse(screen, CAT_COLOR, (80, 240, 30, 40))
    ellipse(screen, BLACK, (80, 240, 30, 40), 1)
    ellipse(screen, CAT_COLOR, (100, 260, 70, 40))
    ellipse(screen, BLACK, (100, 260, 70, 40), 1)
    polygon(screen, CAT_COLOR, [(75,170), (80,190),(97,175)])
    polygon(screen, CAT_COLOR, [(140,170), (160,160),(160,180)])
    polygon(screen, BLACK, [(75,170), (80,190),(97,175)], 1)
    polygon(screen, BLACK, [(140,170), (160,160),(160,180)], 1)
    polygon(screen, (247, 193, 181), [(80,175), (82,190),(97,175)])
    polygon(screen, (247, 193, 181), [(145,175), (158,166),(160,180)])
    polygon(screen, BLACK, [(80,175), (82,190),(97,175)], 1)
    polygon(screen, BLACK, [(145,175), (158,166),(160,180)], 1)
    circle(screen, (157, 245, 42), (110, 210), 13)
    circle(screen, BLACK, (110, 210), 13, 1)
    circle(screen, (157, 245, 42), (140, 207), 13)
    circle(screen, BLACK, (140, 207), 13, 1)
    ellipse(screen, BLACK, (110, 205, 5, 15))
    ellipse(screen, BLACK, (140, 202, 5, 15))
    line(screen, (255, 255, 255), (140, 205), (133, 198), 4)
    line(screen, (255, 255, 255), (110, 208), (103, 201), 4)
    polygon(screen, (247, 193, 181), [(123,220), (129,220),(126,225)])
    polygon(screen, BLACK, [(123,220), (129,220),(126,225)], 1)
    line(screen, BLACK, (126,225), (126,230), 1)
    arc(screen, BLACK, (100, 205, 30, 30), 17, 18, 1)
    arc(screen, BLACK, (125, 215, 30, 20), 16.5, 17.5, 1)
    arc(screen, BLACK, (70, 225, 90, 90), 1.5, 2.5, 1)
    arc(screen, BLACK, (69, 225, 80, 80), 1.5, 2.5, 1)
    arc(screen, BLACK, (68, 225, 70, 70), 1.5, 2.5, 1)
    arc(screen, BLACK, (90, 225, 100, 100), 0.8, 1.7, 1)
    arc(screen, BLACK, (90, 225, 95, 95), 0.8, 1.7, 1)
    arc(screen, BLACK, (90, 225, 90, 90), 0.8, 1., 1)
    
def clew():
    circle(screen, (15, 91, 245), (60, 350), 30)
    line(screen, BLACK, (35, 340), (85, 360), 3)
    line(screen, BLACK, (35, 345), (80, 365), 3)
    line(screen, BLACK, (35, 350), (70, 370), 3)
    line(screen, BLACK, (35, 355), (65, 375), 3)
    line(screen, BLACK, (60, 323), (55, 340), 3)
    line(screen, BLACK, (70, 325), (65, 345), 3)
    line(screen, BLACK, (80, 330), (75, 350), 3)
    arc(screen, (15, 91, 245), (80, 275, 100, 100), 16, 18, 1)
    arc(screen, (15, 91, 245), (149, 350, 100, 100), 1, 2.4, 1)

    

background() 
cat()
clew()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            finished = True

pygame.quit()
