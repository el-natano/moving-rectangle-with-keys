# Nathan Barton
# shapes in dictionaries
# 3-5-25

import pygame


def draw_circle(screen, color, center, radius):
    pygame.draw.circle(screen, color, center, radius)

def draw_rect(screen, color, position):
    pygame.draw.rect(screen, color, position)

def draw_line (screen, color, shape_width, start, end):
    pygame.draw.line(screen, start, end, color, width=shape_width)

def polygon(screen, color, positionlist):
    pygame.draw.polygon(screen, color, positionlist)
