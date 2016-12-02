#!/usr/bin/env python
# -*- coding: utf-8 

import pygame
import math


SCREEN_SIZE = [700, 600]
MAX_ANGLE = 90
MIN_ANGLE = 0
DELTA_ANGLE = 10
LENGTH_CANNON = 30
POS_CANNON = [1,SCREEN_SIZE[1]-1] 
COLOR_CANNON = [255,0,0]


def angle_to_dx_dy(l,angle):
    dx = math.ceil(l * math.cos(math.radians(angle)))
    dy = math.ceil(l * math.sin(math.radians(angle)))
    return [dx,dy]
    

angle = 45

pygame.init()


size_rect = [10,20]



screen=pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PVO")
pygame.mouse.set_visible(0)

done = False

clock = pygame.time.Clock()

rotate_right = False
rotate_left = False

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                rotate_left = True
                        
            if event.key == pygame.K_RIGHT:
                rotate_right = True


        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT:
                rotate_left = False
                        
            if event.key == pygame.K_RIGHT:
                rotate_right = False
    
    
    
    if rotate_left:
        angle += DELTA_ANGLE
        if angle > MAX_ANGLE :
            angle = MAX_ANGLE
    
    if rotate_right:
        angle -= DELTA_ANGLE            
        if angle < MIN_ANGLE :
            angle = MIN_ANGLE   
            
    screen.fill([255,255,0])
    
    delta = angle_to_dx_dy(LENGTH_CANNON,angle)
    pygame.draw.line(screen,COLOR_CANNON,POS_CANNON,[POS_CANNON[0]+delta[0],POS_CANNON[1]-delta[1]],5)
    
    
    pos =  pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    pygame.draw.rect(screen,[35,240,15],[x,y,size_rect[0],size_rect[1]])
                
                
    pygame.display.flip()       
            
            
    clock.tick(20)

pygame.quit()    
