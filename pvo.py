#!/usr/bin/env python
# -*- coding: utf-8 

import pygame
import math

MAX_ANGLE = 90
MIN_ANGLE = 0
DELTA_ANGLE = 1
LENGTH_CANNON = 30
COLOR_CANNON = [255,0,0]


def angle_to_dx_dy(l,angle):
    dx = math.ceil(l * math.cos(angle))
    dy = math.ceil(l * math.sin(angle))
    return [dx,dy]
    

angle = 45

pygame.init()

size = [700, 600]
size_rect = [10,20]



screen=pygame.display.set_mode(size)
pygame.display.set_caption("PVO")
pygame.mouse.set_visible(0)

done = False

clock = pygame.time.Clock()

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
         
        if event.type == pygame.K_LEFT:
            angle += DELTA_ANGLE
            if angle > MAX_ANGLE :
                angle = MAX_ANGLE
        
        if event.type == pygame.K_RIGHT:
            angle -= DELTA_ANGLE
            print("RIGHT :" + str(angle))
            if angle < MIN_ANGLE :
                angle = MIN_ANGLE        
    
    
            
    screen.fill([255,255,0])
    
    delta = angle_to_dx_dy(LENGTH_CANNON,angle)
    pygame.draw.line(screen,COLOR_CANNON,[0,size[1]],[delta[0],size[1]-delta[1]],2)
    
    
    pos =  pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(screen,[35,240,15],[x,y,size_rect[0],size_rect[1]])
                
                
    pygame.display.flip()       
            
            
    clock.tick(20)

pygame.quit()    
