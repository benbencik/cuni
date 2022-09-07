#!/usr/bin/python

import argparse
import pygame
import sys
import time
import math
import cmath

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
                pygame.draw.line(DISPLAY, COLOR['grey'], (x2, ypos), (x2, ypos+DASH_TYPE[0]))
                ypos += DASH_TYPE[0] + DASH_TYPE[1]
    
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(DISPLAY, COLOR['white'], (0, y), (WIDTH, y))
        for y2 in range(y+DASH_SEPARATION, y+GRID_SIZE, DASH_SEPARATION):
            xpos = 0
            while xpos < WIDTH:
                pygame.draw.line(DISPLAY, COLOR['grey'], (xpos, y2), (xpos+DASH_TYPE[0], y2))
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
GRID_SIZE = 240  # space betweeen solid lines
DASH_SEPARATION = 60  # space between dash lines
DASH_TYPE = (4, 6)  # (dash length, space length)
SAMPLE_RATE = 0.02  # mark trace every n seconds
COLOR = {
    'white': pygame.Color(230, 230, 230),
    'dimm_white': pygame.Color(180, 180, 180),
    'grey': pygame.Color(80, 80, 80),
    'dark_grey': pygame.Color(40, 40, 40),
    'blue': pygame.Color(40, 0, 240),
    'green': pygame.Color(40, 240, 20),
    'pink': pygame.Color(240, 0, 160)
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


final_trace = []
n = 10

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
            if STATE == 1:
                tl = len(trace)
                for i in range(tl):
                    x, y = trace[i]
                    trace[i] = (x-WIDTH//2, y-HEIGHT//2)
                c = []
                for i in range(n, -n-1, -1):
                    l = []
                    for t in range(tl):
                        num1 = cmath.exp(2*math.pi * 1j * i * t/tl)
                        num2 = (trace[t][0] + trace[t][1] * 1j)
                        l.append(num1*num2)
                    c.append(sum(l)/tl)

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
            trace.append(pos)
            DISPLAY.set_at(pos, COLOR['green'])
    
    if STATE == 2:
        time.sleep(0.05)
        DISPLAY.fill(COLOR['dark_grey'])

        z = WIDTH//2 + HEIGHT//2*1j
        l = [n]
        for r in zip(range(n+1, 2*n+1), range(n-1, -1, -1)):
            l.append(r[0])
            l.append(r[1])
        
        for i in l:
            old_z = z
            z += cmath.exp(2*math.pi*1j*(i-n)*t/tl)*c[i] 
            pygame.draw.line(DISPLAY, COLOR['grey'], (old_z.real, old_z.imag), (z.real, z.imag))
            r = ((old_z.real - z.real)**2 + (old_z.imag - z.imag)**2)**0.5
            if r > 1:
                pygame.draw.circle(DISPLAY, COLOR['grey'], (int(old_z.real), int(old_z.imag)), int(r), 1)
       

        if len(final_trace) < tl:
            final_trace.append(z)
        
        for p in trace:
            DISPLAY.set_at((int(p[0]+WIDTH//2), int(p[1]+HEIGHT//2)), COLOR['green'])
        for i in range(len(final_trace)):
            p = final_trace[i]
            DISPLAY.set_at((int(p.real), int(p.imag)), COLOR["pink"])
    
        t = (t+1) % tl
    pygame.display.update()
        