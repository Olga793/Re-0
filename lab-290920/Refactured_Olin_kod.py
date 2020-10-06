# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 11:01:14 2020

@author: Ольга
"""

import numpy as np
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
GX = 800
GY = 800
screen = pygame.display.set_mode((GX, GY))

CAT_COLOR = (250, 155, 12)
EYE_COLOR = (157, 245, 42)
EAR_COLOR = (247, 193, 181)
WOOL_COLOR = (15, 91, 245)
WINDOW_COLOR = (42, 221, 245)
FLOOR_COLOR = (105, 65, 5)
BLACK = (0, 0, 0)

def draw_window(x, y):
    polygon(screen, (255, 255, 255), [(x-100, y-75), (x+100, y-75), (x+100, y+105), (x-100, y+105)])
    polygon(screen, WINDOW_COLOR, [(x-90, y-70), (x, y-70), (x, y-5), (x-90, y-5)])
    polygon(screen, WINDOW_COLOR, [(x+5, y-70), (x+90, y-70), (x+90, y-5), (x+5, y-5)])
    polygon(screen, WINDOW_COLOR, [(x-90, y+5), (x, y+5), (x, y+100), (x-90, y+100)])
    polygon(screen, WINDOW_COLOR, [(x+5, y+5), (x+90, y+5), (x+90, y+100), (x+5, y+100)])

def background():
    draw_window(520, 200)
    draw_window(240, 200)
    rect(screen, FLOOR_COLOR, (0, GY//2, GX, GY//2))


def tail(x, y, r, alpha):
    a = []
    for t in range(6283):
    	b = [2*r*np.cos(t/1000), r*np.sin(t/1000)]
    	a.append((x + b[0]*np.cos(alpha) + b[1]*np.sin(alpha),
    	y - b[0]*np.sin(alpha) + b[1]*np.cos(alpha)))
    polygon(screen, CAT_COLOR, a, 0)
    polygon(screen, BLACK, a, 1)
    
def eye(x, y, r):
    circle(screen, EYE_COLOR, (x, y), r)
    circle(screen, BLACK, (x, y), r, 1)
    ellipse(screen, BLACK, (x+r/3, y-2*r/3, r/3, 4*r/3))
    line(screen, (255, 255, 255), (x+r/3, y), (x-r/3, y-2*r/3), r//3)

def newarc(x, y, r, start, phi, n):
    a = []
    for t in range(int(start*n), int((start+phi)*n)):
    	a.append((x + r*np.cos(t/n), y + r*np.sin(t/n)))
    aalines(screen, BLACK, False, a, 1)


def face(x, y, r):
    #глаза
    eye(x - (4*r)/3, y - r, r)
    eye(x + (4*r)/3, y - r, r)
    
    #нос
    polygon(screen, EAR_COLOR, [(x-r/5, y), (x+r/5, y), (x, y+r/3)])
    polygon(screen, BLACK, [(x-r/5, y), (x+r/5, y), (x, y+r/3)], 1)
    
    #рот
    newarc(x-10, y, r, np.pi/4, 7*np.pi/12, 15)
    newarc(x+10, y, r, np.pi/6, 7*np.pi/12, 15)
    line(screen, BLACK, (x, y + r/3), (x, y + 2*r/3), 1)
    
    #усы
    arc(screen, BLACK, (x-4*r, y+r/3, 6*r, 6*r), 1.5, 2.5, 1)
    arc(screen, BLACK, (x-4*r, y+r/3, 6*r-2*r/3, 6*r-2*r/3), 1.5, 2.5, 1)
    arc(screen, BLACK, (x-4*r, y+r/3, 6*r-4*r/3, 6*r-4*r/3), 1.5, 2.5, 1)
    
    arc(screen, BLACK, (x-2*r, y+r/3, 6*r+2*r/3, 6*r+2*r/3), 0.8, 1.7, 1)
    arc(screen, BLACK, (x-2*r, y+r/3, 6*r+r/3, 6*r+r/3), 0.8, 1.7, 1)
    arc(screen, BLACK, (x-2*r, y+r/3, 6*r, 6*r), 0.8, 1.7, 1)


def draw_head(x, y, r):
    #голова
    circle(screen, CAT_COLOR, (x, y), r)
    circle(screen, BLACK, (x, y), r, 1)
    
    #уши
    ear1 = [(x + r*np.sin(np.pi/12), y - r*np.cos(np.pi/12)),
    (x + r*np.sin(3*np.pi/12), y - r*np.cos(3*np.pi/12)), 
    (x + (3*r/2)*np.sin(np.pi/6), y - (3*r/2)*np.cos(np.pi/6))]
    ear2 = [(x - r*np.sin(np.pi/12), y - r*np.cos(np.pi/12)),
    (x - r*np.sin(3*np.pi/12), y - r*np.cos(3*np.pi/12)), 
    (x - (3*r/2)*np.sin(np.pi/6), y - (3*r/2)*np.cos(np.pi/6))]
    
    for ear in [ear1, ear2]:
    	polygon(screen, CAT_COLOR, ear)
    	polygon(screen, BLACK, ear, 1)
    
    face(x, y+(3*r)//10, (3*r)//10)


def cat(x, y, r):
    tail(x+6*r, y+r, r, -np.pi/6)
    
    #туловище
    ellipse(screen, CAT_COLOR, (x-5*r, y-2.5*r, 10*r, 5*r))
    ellipse(screen, BLACK, (x-5*r, y-2.5*r, 10*r, 5*r), 1)
    
    #задняя лапа
    circle(screen, CAT_COLOR, (x+3*r, y+r), 1.5*r)
    circle(screen, BLACK, (x+3*r, y+r), 1.5*r, 1)
    ellipse(screen, CAT_COLOR, (x+3.8*r, y+0.8*r, r, 3*r))
    ellipse(screen, BLACK, (x+3.8*r, y+0.8*r, r, 3*r), 1)
    
    #передняя лапа
    ellipse(screen, CAT_COLOR, (x-5*r, y+r, 3*r, 8*r/5))
    ellipse(screen, BLACK, (x-5*r, y+r, 3*r, 8*r/5), 1)
    
    draw_head(x-4*r, y-r, 2*r)
    
    
def clew(x, y, r):
    circle(screen, WOOL_COLOR, (x, y), 6*r)
    l = 3*r//5
    line(screen, BLACK, (x-5*r, y-2*r), (x+5*r, y+2*r), l)
    line(screen, BLACK, (x-5*r, y-r), (x+4*r, y+3*r), l)
    line(screen, BLACK, (x-5*r, y), (x+2*r, y+4*r), l)
    line(screen, BLACK, (x-5*r, y+r), (x+r, y+5*r), l)
    line(screen, BLACK, (x, y-5*r), (x-r, y-2*r), l)
    line(screen, BLACK, (x+2*r, y-5*r), (x+r, y-r), l)
    line(screen, BLACK, (x+4*r, y-4*r), (x+3*r, y-r), l)
    arc(screen, WOOL_COLOR, (x+4*r, y-15*r, 20*r, 20*r), 16, 18, 1)
    arc(screen, WOOL_COLOR, (x+17*r, y, 20*r, 20*r), 1, 2.4, 1)

    

background() 
cat(650, 500, 25)
CAT_COLOR = (108, 93, 83)
EYE_COLOR = (42, 212, 255)
cat(300, 600, 30)
clew(60, 700, 5)
WOOL_COLOR = (91, 245, 15)
clew(100, 450, 5)
WOOL_COLOR = (15, 245, 91)
clew(500, 750, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            finished = True

pygame.quit()
