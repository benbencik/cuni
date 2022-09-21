#!/usr/bin/python

import sys
import time
import cmath
import pygame
import argparse
import svgpathtools



class Window():
    def __init__(self, resolution) -> None:
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Courier New', 20)
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
        self.color_decay = 0.8
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
            'ESC to exit R to reset',
            'C, L, P to toggle circles, lines, points'
        ]
        ypos = canvas.height // 2 - 50
        for i in range(len(message)):
            text = self.font.render(message[i], True, self.font_color)
            self.display.blit(
                text, ((self.width - text.get_width())//2, ypos + i*text.get_height()))

    def reset(self):
        self.display.fill(canvas.color['dark_grey'])
        self.draw_grid()
        self.print_welcome_text()

    def fade_color(self, i, ttime, trace_len):
        instensity = (ttime - i) % trace_len
        alpha = self.color_decay * instensity / trace_len
        return self.curve_color.lerp(self.bg_color, alpha)


class FourierTransform():
    def __init__(self, w, h, n):
        self.width = w
        self.height = h
        self.n = n // 2  # number of functions

        self.time = 0
        self.trace = []
        self.aprox_trace = []
        self.coefficients = []
        self.draw_last_line = False

        self.toggle_lines = True
        self.toggle_circles = True
        self.toggle_points = True
        self.zoom = 1
        self.center = [canvas.width//2, canvas.height//2]
        self.offset = [0, 0]

    def calculate_coeficients(self):
        # condition needs to be satisfied otherwise the algorithm malfunctions
        # for higher percision increase number of points traced
        if len(self.trace) < self.n*2: self.n = len(self.trace)//2 

        # transpose points 
        for i in range(len(self.trace)):
            x, y = self.trace[i]
            self.trace[i] = (x-canvas.width//2, y-canvas.height//2)

        # coeficients deretmine initial angle and magnitude
        self.coefficients = []
        for freq in range(self.n, -self.n-1, -1):
            l = []
            for t in range(len(self.trace)):
                num1 = cmath.exp(2*cmath.pi * 1j * freq * t/len(self.trace))
                num2 = (self.trace[t][0] + self.trace[t][1] * 1j)
                l.append(num1*num2)
            self.coefficients.append(sum(l)/len(self.trace))

    def calculate_point(self):
        z = canvas.width//2 + canvas.height//2*1j
        
        # zip together frequencies by positive negative pairs
        frequency = [0]
        neg_range = range(-1, -self.n-1, -1)
        pos_range = range(1, self.n+1)
        for r in zip(neg_range, pos_range): frequency += r

        for freq in frequency:
            old_z = z
            # coeficient defining stgarting angle and magnitude
            complex_coef = self.coefficients[freq+self.n]
            ttime = self.time / len(self.trace)
            # add new function to resulting complex point
            z += complex_coef * cmath.exp(freq * ttime * 2*cmath.pi*1j)
            
            # draw resulting vector
            x1, y1 = self.zoom_point(old_z.real, old_z.imag)
            x2, y2 = self.zoom_point(z.real, z.imag)
            if self.toggle_lines:
                pygame.draw.line(canvas.display, canvas.color['grey'], 
                                (x1, y1), (x2, y2))
            # if self.toggle_lines:
            #     pygame.draw.line(canvas.display, canvas.color['grey'], 
            #                     (old_z.real, old_z.imag), (z.real, z.imag))
            
            if self.toggle_circles:
                r = cmath.sqrt((x1 - x2)**2 + (y1 - y2)**2).real
                if r > 1:
                    pygame.draw.circle(canvas.display, canvas.color['grey'], 
                                    (int(x1), int(y1)), int(r), 1)

            # draw circle described by the vector above
            # if self.toggle_circles:
            #     r = cmath.sqrt((old_z.real - z.real)**2 + (old_z.imag - z.imag)**2).real
            #     if r > 1:
            #         pygame.draw.circle(canvas.display, canvas.color['grey'], 
            #                         (int(old_z.real), int(old_z.imag)), int(r), 1)
        self.center = [z.real, z.imag]
        self.offset = [self.center[0]-canvas.width/2, self.center[1]-canvas.height/2]
        if len(self.aprox_trace) < len(self.trace): self.aprox_trace.append(z)

    def draw_curve(self):
        range_end = len(self.aprox_trace)
        if self.draw_last_line:
            range_end = len(self.aprox_trace)+1
        elif self.time == len(self.trace)-1:
            self.draw_last_line = True
        
        # draw approximated curve
        for i in range(1, range_end):
            color = canvas.fade_color(i, self.time, len(self.trace))
            # p1, p2 = self.aprox_trace[i-1], self.aprox_trace[i%len(self.aprox_trace)]
            x1, y1 = self.zoom_point(self.aprox_trace[i-1].real, self.aprox_trace[i-1].imag)
            x2, y2 = self.zoom_point(self.aprox_trace[i%len(self.aprox_trace)].real, self.aprox_trace[i%len(self.aprox_trace)].imag)       
            pygame.draw.line(canvas.display, color, (int(x1), int(y1)), (int(x2), int(y2)))

        # draw traced points
        if self.toggle_points:
            for p in self.trace:
                x, y = int(p[0]+canvas.width/2), int(p[1]+canvas.height/2)
                canvas.display.set_at((x, y), canvas.trace_color)

        self.time = (self.time+1) % len(self.trace)
    
    def zoom_point(self, x, y):
        x = self.center[0]*(1 - self.zoom) + x * self.zoom #+ self.offset[0]
        y = self.center[1]*(1 - self.zoom) + y * self.zoom #+ self.offset[1]
        return x, y
        

    def record_point(self):
        pos = pygame.mouse.get_pos()
        if self.trace[-1] != pos:
            self.trace.append(pos)
            canvas.display.set_at(pos, canvas.trace_color)

    def reset(self):
        self.trace = []
        self.aprox_trace = []
        self.coefficients = []
        self.time = 0
        self.draw_last_line = False
        self.zoom = 1


def extract_svg():
    paths, attributes, svg_attributes = svgpathtools.svg2paths2(args.input_file)
    image_w, image_h = map(int, svg_attributes['viewBox'].split(' ')[2:])
    
    for attr in attributes:
        # extracting only the features wich are strokes
        if attr.get('d') and attr.get('stroke'):
            svgpath = attr['d']
            path = svgpathtools.parse_path(svgpath)
            POINTS_PER_PATH = args.point_density
            
            # sample points from the line
            for i in range(0, POINTS_PER_PATH+1):
                f = i/POINTS_PER_PATH
                complex_point = path.point(f)
                # append points transposed to canvas size
                ft.trace.append((complex_point.real/image_w*canvas.width,
                                complex_point.imag/image_h*canvas.height))

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-r', '--resolution', nargs=2, help='set width and height of the window, default is fullscreen')
arg_parser.add_argument('-i', '--input-file', type=str, help='specify a .svg file for trace')
arg_parser.add_argument('-n', '--num-of-functions', type=int, default=100, help='number of functions used to approximate the curve')
arg_parser.add_argument('-s', '--sampling-rate', type=int, default=100, help='mark trace of curve every n miliseconds')
arg_parser.add_argument('-u', '--update-rate', type=int, default=50, help='one frame will take n miliseconds')
arg_parser.add_argument('-d', '--point-density', type=int, default=200, help='number of point samples per path')
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
SAMPLE_RATE = args.sampling_rate / 10e3  # mark trace every n miliseconds
UPDATE_RATE = args.update_rate / 10e2  # move through time everty n miliseconds

if args.input_file: 
    extract_svg()
    ft.calculate_coeficients()
    STATE = 2  # trace is recorded skip 1 state
else:
    canvas.draw_grid()
    canvas.print_welcome_text()
    pygame.display.update()


prev_time, current_time = 0, 0
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
        if e.type == pygame.KEYDOWN and e.key == pygame.K_p:
            ft.toggle_points = not ft.toggle_points
        if e.type == pygame.KEYDOWN and e.key == pygame.K_l:
            ft.toggle_lines = not ft.toggle_lines
        if e.type == pygame.KEYDOWN and e.key == pygame.K_c:
            ft.toggle_circles = not ft.toggle_circles
        if e.type == pygame.KEYDOWN and e.key == pygame.K_z:
            ft.zoom += 0.1
            print(ft.zoom)
        if e.type == pygame.KEYDOWN and e.key == pygame.K_x:
            ft.zoom -= 0.1
            print(ft.zoom)

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
