#!/usr/bin/python

import argparse
import pygame
import sys
import time


def window_resolution(args):
    if args.resolution:
        return int(args.resolution[0]), int(args.resolution[1])
    else:
        return pygame.display.Info().current_w, pygame.display.Info().current_h

def drawing_grid(block_size, dash_size, dash_type):
    # make grid
    for x in range(0, WIDTH, block_size):
        pygame.draw.line(DISPLAY, COLOR['white'], (x, 0), (x, HEIGHT))
        for x2 in range(x+dash_size, x+block_size, dash_size):
            ypos = 0
            while ypos < HEIGHT:
                pygame.draw.line(DISPLAY, COLOR['dimm_white'], (x2, ypos), (x2, ypos+dash_type[0]))
                ypos += dash_type[0] + dash_type[1]
    
    for y in range(0, HEIGHT, block_size):
        pygame.draw.line(DISPLAY, COLOR['white'], (0, y), (WIDTH, y))
        for y2 in range(y+dash_size, y+block_size, dash_size):
            xpos = 0
            while xpos < WIDTH:
                pygame.draw.line(DISPLAY, COLOR['dimm_white'], (xpos, y2), (xpos+dash_type[0], y2))
                xpos += dash_type[0] + dash_type[1]

    
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-r', '--resolution', nargs=2)
args = arg_parser.parse_args()


pygame.init()
pygame.font.init()
WIDTH, HEIGHT = window_resolution(args)
COLOR = {
    'white': pygame.Color(230, 230, 230),
    'dimm_white': pygame.Color(180, 180, 180),
    'grey': pygame.Color(80, 80, 80),
    'dark_grey': pygame.Color(40, 40, 40),
    'blue': pygame.Color(40, 0, 240)
}
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY.fill(COLOR['dark_grey'])
drawing_grid(200, 50, (1,9))

# welcome text
font = pygame.font.SysFont('Courier New', 30)
drawing = font.render("press SPACE to start/stop drawing", True, COLOR['blue'])
quit = font.render("press ESC to exit", True, COLOR['blue'])
DISPLAY.blit(drawing, ((WIDTH - drawing.get_width())//2, (HEIGHT - drawing.get_height())//2 - 30))
DISPLAY.blit(quit, ((WIDTH - quit.get_width())//2, (HEIGHT - quit.get_height())//2 + 30))

pygame.display.update()


while True:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit()