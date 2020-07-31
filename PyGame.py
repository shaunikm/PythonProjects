#!/usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *

# Define some colors
white = (255, 255, 255)

pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode((1920, 1080))

org_pic = pygame.image.load('C:\\Users\\shaun\\Desktop\\spacecraft-rocket-cartoon-ship-cartoon-rocket-launch-png-clip-art.png').convert()
pic_position_and_size = org_pic.get_rect()
pic = pygame.transform.scale(org_pic, pic_position_and_size.size)
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Clear event queue
pygame.event.clear()

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

        if event.type != KEYDOWN:
            # background in white
            screen.fill(white)

            # Copy image to screen:
            screen.blit(pic, (0, 0))

            # Update the screen with what we've drawn.
            pygame.display.flip()
            pygame.display.update()

            pygame.time.delay(10)  # stop the program for 1/100 second

            # decreases size by 1 pixel in x and y axis
            pic_position_and_size = pic_position_and_size.inflate(-1, -1)

            # scales the image
            pic = pygame.transform.smoothscale(org_pic, pic_position_and_size.size)
    clock.tick(60)

# Close the window and quit.
pygame.quit()