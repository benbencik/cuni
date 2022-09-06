#!/usr/bin/python

import argparse
from cgitb import reset
import pygame
import sys
import time


def window_resolution(args):
    if args.resolution:
        return int(args.resolution[0]), int(args.resolution[1])
    else:
        return pygame.display.Info().current_w, pygame.display.Info().current_h

def draw_grid():
    # make grid
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(DISPLAY, COLOR['white'], (x, 0), (x, HEIGHT))
        for x2 in range(x+DASH_SEPARATION, x+GRID_SIZE, DASH_SEPARATION):
            ypos = 0
            while ypos < HEIGHT:
                pygame.draw.line(DISPLAY, COLOR['dimm_white'], (x2, ypos), (x2, ypos+DASH_TYPE[0]))
                ypos += DASH_TYPE[0] + DASH_TYPE[1]
    
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(DISPLAY, COLOR['white'], (0, y), (WIDTH, y))
        for y2 in range(y+DASH_SEPARATION, y+GRID_SIZE, DASH_SEPARATION):
            xpos = 0
            while xpos < WIDTH:
                pygame.draw.line(DISPLAY, COLOR['dimm_white'], (xpos, y2), (xpos+DASH_TYPE[0], y2))
                xpos += DASH_TYPE[0] + DASH_TYPE[1]

    # center
    line_length = 20
    pygame.draw.line(DISPLAY, COLOR['green'], 
                    (WIDTH/2 - line_length, HEIGHT/2), 
                    (WIDTH/2 + line_length, HEIGHT/2))
    pygame.draw.line(DISPLAY, COLOR['green'], 
                    (WIDTH/2, HEIGHT/2 - line_length), 
                    (WIDTH/2, HEIGHT/2 + line_length))


def print_welcome_text():
    message = [
        'press SPACE to start/stop drawing',
        'press ESC to exit',
        'press R to reset'
        ]
    ypos = 100
    for i in range(len(message)):
        text = FONT.render(message[i], True, COLOR['green'])
        DISPLAY.blit(text, ((WIDTH - text.get_width())//2, ypos + i*text.get_height()))

    
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-r', '--resolution', nargs=2)
args = arg_parser.parse_args()

pygame.init()
pygame.font.init()

FONT = pygame.font.SysFont('Courier New', 30)
WIDTH, HEIGHT = window_resolution(args)
GRID_SIZE = 200  # space betweeen solid lines
DASH_SEPARATION = 50  # space between dash lines
DASH_TYPE = (1, 9)  # (dash length, space length)
SAMPLE_RATE = 0.02  # mark trace every n seconds
COLOR = {
    'white': pygame.Color(230, 230, 230),
    'dimm_white': pygame.Color(180, 180, 180),
    'grey': pygame.Color(80, 80, 80),
    'dark_grey': pygame.Color(40, 40, 40),
    'blue': pygame.Color(40, 0, 240),
    'green': pygame.Color(40, 240, 20)
}
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY.fill(COLOR['dark_grey'])
draw_grid()
print_welcome_text()

pygame.display.update()
prev_time = 0  # time of previously marked trace
STATE = 0
""" 
application might be in 3 different STATEs
0: idle
1: drawing
2: running
"""

while True:
    current_time = time.monotonic()

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and STATE < 2:
            DISPLAY.fill(COLOR['dark_grey'])
            if STATE == 0:
                draw_grid() 
                trace = [pygame.mouse.get_pos()]
                prev_time = time.monotonic()
            STATE += 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            STATE = 0
            DISPLAY.fill(COLOR['dark_grey'])
            draw_grid()
            print_welcome_text()
    
    if STATE == 1 and current_time - prev_time >= SAMPLE_RATE:
        pos = pygame.mouse.get_pos()
        prev_time = current_time
        if trace[-1] != pos:
            print(current_time) 
            trace.append(pos)
            DISPLAY.set_at(pos, COLOR['green'])
    pygame.display.update()
        