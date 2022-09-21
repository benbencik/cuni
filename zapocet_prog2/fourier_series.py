#!/usr/bin/python

import argparse
import pygame
import sys
import time
import math
import cmath
import svgpathtools
import svgutils


class Window():
    def __init__(self, resolution) -> None:
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Courier New', 15)
        self.width, self.height = self.window_resolution(resolution)
        self.grid_size = 240  # space betweeen solid lines
        self.dash_separation = 60  # space between dash lines
        self.dash_type = (4, 6)  # (dash length, space length)
        self.color = {
            'white': pygame.Color(230, 230, 230),
            'dimm_white': pygame.Color(180, 180, 180),
            'grey': pygame.Color(100, 100, 100),
            'dark_grey': pygame.Color(40, 40, 40),
            'blue': pygame.Color(40, 0, 240),
            'green': pygame.Color(40, 240, 20),
            'pink': pygame.Color(240, 0, 160)
        }
        self.color_decay = 0.98
        self.bg_color = self.color['dark_grey']
        self.curve_color = self.color['pink']
        self.trace_color = self.color['green']
        self.font_color = self.color['green']

        self.display = pygame.display.set_mode((self.width, self.height))
        self.display.fill(self.bg_color)

    def window_resolution(self, resolution):
        if resolution:
            return int(resolution[0]), int(resolution[1])
        else:
            return pygame.display.Info().current_w, pygame.display.Info().current_h

    def draw_grid(self):
        # make grid
        for x in range(0, self.width, self.grid_size):
            pygame.draw.line(
                self.display, self.color['white'], (x, 0), (x, self.height))
            for x2 in range(x+self.dash_separation, x+self.grid_size, self.dash_separation):
                ypos = 0
                while ypos < self.height:
                    pygame.draw.line(
                        self.display, self.color['grey'], (x2, ypos), (x2, ypos+self.dash_type[0]))
                    ypos += self.dash_type[0] + self.dash_type[1]

        for y in range(0, self.height, self.grid_size):
            pygame.draw.line(
                self.display, self.color['white'], (0, y), (self.width, y))
            for y2 in range(y+self.dash_separation, y+self.grid_size, self.dash_separation):
                xpos = 0
                while xpos < self.width:
                    pygame.draw.line(
                        self.display, self.color['grey'], (xpos, y2), (xpos+self.dash_type[0], y2))
                    xpos += self.dash_type[0] + self.dash_type[1]

    def print_welcome_text(self):
        message = [
            'press SPACE to start/stop drawing',
            'press ESC to exit',
            'press R to reset'
        ]
        ypos = canvas.height // 2
        for i in range(len(message)):
            text = self.font.render(message[i], True, self.font_color)
            self.display.blit(
                text, ((self.width - text.get_width())//2, ypos + i*text.get_height()))

    def reset(self):
        self.display.fill(canvas.color['dark_grey'])
        self.draw_grid()
        self.print_welcome_text()

    def fade_color(self, i, t, tl):
        instensity = (t - i + tl) % tl
        alpha = self.color_decay * instensity / tl
        return self.curve_color.lerp(self.bg_color, alpha)


class FourierTransform():
    def __init__(self, w, h, n):
        self.width = w
        self.height = h
        self.number_of_functions = n//2

        self.t = 0
        self.trace = []
        self.tl = []
        self.final_trace = []
        self.coefficients = []

        self.center = [0, 0]
        self.follow = True
        self.zoom = 100

    def calculate_coeficients(self):
        self.tl = len(self.trace)
        for i in range(self.tl):
            x, y = self.trace[i]
            self.trace[i] = (x-canvas.width//2, y-canvas.height//2)
        self.coefficients = []
        for i in range(ft.number_of_functions, -ft.number_of_functions-1, -1):
            l = []
            for t in range(self.tl):
                num1 = cmath.exp(2*math.pi * 1j * i * t/self.tl)
                num2 = (self.trace[t][0] + self.trace[t][1] * 1j)
                l.append(num1*num2)
            self.coefficients.append(sum(l)/self.tl)

    def record_point(self):
        pos = pygame.mouse.get_pos()
        if self.trace[-1] != pos:
            self.trace.append(pos)
            canvas.display.set_at(pos, canvas.trace_color)

    def calculate_point(self):
        z = canvas.width//2 + canvas.height//2*1j
        l = [self.number_of_functions]
        for r in zip(range(self.number_of_functions+1, 2*self.number_of_functions+1), range(self.number_of_functions-1, -1, -1)):
            l.append(r[0])
            l.append(r[1])

        for i in l:
            old_z = z
            z += cmath.exp(2*math.pi*1j*(i-self.number_of_functions)
                           * self.t / self.tl)*self.coefficients[i]
            pygame.draw.line(
                canvas.display, canvas.color['grey'], (old_z.real, old_z.imag), (z.real, z.imag))
            r = ((old_z.real - z.real)**2 + (old_z.imag - z.imag)**2)**0.5
            if r > 1:
                pygame.draw.circle(canvas.display, canvas.color['grey'], (int(
                    old_z.real), int(old_z.imag)), int(r), 1)

        self.center = [z.real, z.imag]
        if len(self.final_trace) < self.tl:
            self.final_trace.append(z)

    def draw_curve(self):
        # draw plotted line
        # treba to uzavrieť
        for i in range(1, len(self.final_trace)):
            color = canvas.fade_color(i, self.t, self.tl)
            p1, p2 = self.final_trace[i-1], self.final_trace[i]
            pygame.draw.line(canvas.display, color, (int(
                p1.real), int(p1.imag)), (int(p2.real), int(p2.imag)))

        # draw marked points
        for p in self.trace:
            x = p[0]
            y = p[1]
            canvas.display.set_at(
                (int(x+canvas.width/2), int(y+canvas.height/2)), canvas.trace_color)

        self.t = (self.t+1) % self.tl

    def zoom_points(self, x, y):
        slope = (self.center[0] - x) / (self.center[1] - y)
        offset = y - slope*x
        # if x > self.center[0]: x += self.zoom
        # else: x -= self.zoom
        x += self.zoom
        return x, x*slope+offset

    def reset(self):
        self.trace = []
        self.final_trace = []
        self.coefficients = []
        self.t = 0


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-r', '--resolution', nargs=2,
                        help='set width and height of the window')
arg_parser.add_argument('-i', '--input-file', type=str,
                        help='specify a .svg file for trace')
arg_parser.add_argument('-n', '--num-of-functions', type=int, default=100,
                        help='number of functions used to approximate the curve')
arg_parser.add_argument('-s', '--sampling-rate', type=int,
                        default=100, help='mark trace of curve every n miliseconds')
arg_parser.add_argument('-u', '--update-rate', type=int,
                        default=50, help='one frame will take n miliseconds')
args = arg_parser.parse_args()

canvas = Window(args.resolution)
ft = FourierTransform(canvas.width, canvas.height, args.num_of_functions)

""" 
application might be in 3 different STATEs
0: idle
1: recording points
2: running
"""
STATE = 0
prev_time = 0  # time of previously marked trace
SAMPLE_RATE = args.sampling_rate / 10e3  # mark trace every n miliseconds
UPDATE_RATE = args.update_rate / 10e3  # move through time everty n miliseconds

if args.input_file: 
    paths, attributes, svg_attributes = svgpathtools.svg2paths2(args.input_file)
    image_w, image_h = map(int, svg_attributes['viewBox'].split(' ')[2:])
    
    STATE = 2
    for idx, attr in enumerate(attributes):
        # extracting only the features wich are strokes
        if attr.get('d') and attr.get('stroke'):
            svgpath = attr['d']
            path = svgpathtools.parse_path(svgpath)
            LINE_SEGMENTS = 100  # number of line segments to draw
            
            # sample points from the line
            for i in range(0, LINE_SEGMENTS+1):
                f = i/LINE_SEGMENTS
                complex_point = path.point(f)
                # append points transposed to canvas size
                ft.trace.append((complex_point.real/image_w*canvas.width,
                                complex_point.imag/image_h*canvas.height))
    ft.calculate_coeficients()
else:
    canvas.draw_grid()
    canvas.print_welcome_text()

pygame.display.update()


while True:
    current_time = time.monotonic()

    # catch events
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and STATE < 2:
            canvas.display.fill(canvas.bg_color)
            if STATE == 0:
                canvas.draw_grid()
                ft.trace = [pygame.mouse.get_pos()]
                prev_time = current_time
            if STATE == 1:
                ft.calculate_coeficients()
            STATE += 1
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            STATE = 0
            canvas.reset()
            ft.reset()

    if STATE == 1 and current_time - prev_time >= SAMPLE_RATE:
        prev_time = current_time
        ft.record_point()

    if STATE == 2 and current_time - prev_time >= UPDATE_RATE:
        prev_time = current_time
        canvas.display.fill(canvas.bg_color)
        ft.calculate_point()
        ft.draw_curve()

    pygame.display.update()

# zoom needs to be recalculated in every itteration
