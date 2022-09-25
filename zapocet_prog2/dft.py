#!/usr/bin/python

import sys
import time
import cmath
import argparse

import pygame
import svgpathtools


class Window():
    def __init__(self, resolution) -> None:
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Courier New', 20)
        self.font_info = pygame.font.SysFont('Courier New', 15)
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
            'C, L, P to toggle circles, lines, points',
            'press SPACE to start/stop drawing',
            'ESC to exit R to reset',
            '↑/↓ to zoom in/out'
        ]
        ypos = self.height // 2 - 100
        for i, msg in enumerate(message):
            text = self.font.render(msg, True, self.font_color)
            self.display.blit(
                text, ((self.width - text.get_width())//2, ypos + i*text.get_height()))

    def print_stats(self, scale, vectors):
        for arr in arrows:
            if arr['key'] in [pygame.K_LEFT, pygame.K_RIGHT]:
                vectors += arr['delta']
        message = [f"Zoom: {round(scale, 2)}", f"#Vectors: {vectors*2}"]
        xpos, ypos = 20, self.width/30
        for i, msg in enumerate(message):
            text = self.font.render(msg, True, self.font_color)
            self.display.blit(text, ((xpos, ypos + i*text.get_height())))

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
        self.trace_l = 0
        self.aprox_trace = []
        self.coefficients = []
        self.draw_last_line = False

        self.toggle_lines = True
        self.toggle_circles = True
        self.toggle_points = True
        self.zoom = 1
        self.center = [canvas.width//2, canvas.height//2]
        self.offset = [0, 0]
        self.color_shift = 0

    def calculate_coeficients(self):
        self.trace_l = len(self.trace)
        # condition needs to be satisfied otherwise the algorithm malfunctions
        # for higher percision increase number of points traced
        if self.trace_l < self.n*2:
            self.n = self.trace_l//2

        # coeficients deretmine initial angle and magnitude
        self.coefficients = []
        # for k in range(self.n, -self.n-1, -1):
        for k in range(-self.n, self.n+1):
            sum_of_terms = 0
            for t in range(self.trace_l):
                num1 = cmath.exp(-k * t/self.trace_l * 2*cmath.pi * 1j)
                num2 = (self.trace[t][0] + self.trace[t][1] * 1j)
                sum_of_terms += num1*num2
            self.coefficients.append(sum_of_terms/self.trace_l)

    def calculate_point(self):
        z = canvas.width//2 + canvas.height//2*1j

        # zip together frequencies by positive negative pairs
        frequency = [0]
        neg_range = range(-1, -self.n-1, -1)
        pos_range = range(1, self.n+1)
        for r in zip(neg_range, pos_range):
            frequency += r

        for freq in frequency:
            old_z = z
            # coeficient defining stgarting angle and magnitude
            complex_coef = self.coefficients[freq+self.n]
            ttime = self.time / self.trace_l
            # add new function to resulting complex point
            z += complex_coef * cmath.exp(freq * ttime * 2*cmath.pi*1j)

            # draw resulting vector
            p1 = self.zoom_point(old_z)
            p2 = self.zoom_point(z)
            if self.toggle_lines:
                pygame.draw.line(canvas.display, canvas.color['grey'],
                                 (int(p1.real), int(p1.imag)), (int(p2.real), int(p2.imag)))
            if self.toggle_circles:
                r = cmath.sqrt((p1.real - p2.real)**2 +
                               (p1.imag - p2.imag)**2).real
                if r > 1:
                    pygame.draw.circle(canvas.display, canvas.color['grey'],
                                       (int(p1.real), int(p1.imag)), int(r), 1)

        self.center = [z.real, z.imag]
        self.offset = [self.center[0]-canvas.width /
                       2, self.center[1]-canvas.height/2]
        if len(self.aprox_trace) < self.trace_l:
            self.aprox_trace.append(z)

    def draw_curve(self):
        range_end = len(self.aprox_trace)
        if self.draw_last_line:
            range_end = len(self.aprox_trace)+1
        elif self.time-self.color_shift == self.trace_l-1:
            self.draw_last_line = True

        # draw approximated curve
        for i in range(1, range_end):
            color = canvas.fade_color(i, self.time-self.color_shift, self.trace_l)
            p1 = self.zoom_point(self.aprox_trace[i-1])
            p2 = self.zoom_point(self.aprox_trace[i % len(self.aprox_trace)])
            pygame.draw.line(canvas.display, color, (int(
                p1.real), int(p1.imag)), (int(p2.real), int(p2.imag)))

        # draw traced points
        if self.toggle_points:
            for p in self.trace:
                p = self.zoom_point(p[0]+canvas.width /
                                    2 + 1j*(p[1]+canvas.height/2))
                canvas.display.set_at(
                    (int(p.real), int(p.imag)), canvas.trace_color)

        self.time = (self.time+1) % self.trace_l

    def zoom_point(self, point):
        if round(self.zoom, 2) == 1:
            return point
        return (self.center[0]*(1 - self.zoom) + point.real * self.zoom) + \
            1j*(self.center[1]*(1 - self.zoom) + point.imag * self.zoom)

    def record_point(self):
        # pos = pygame.mouse.get_pos()
        # if self.trace[-1] != pos:
        #     self.trace.append(pos)ace_color)
        pos = pygame.mouse.get_pos()
        shifted_pos = [pos[0] - canvas.width//2, pos[1] - canvas.height//2]
        if self.trace[-1] != shifted_pos:
            self.trace.append(shifted_pos)
            canvas.display.set_at(pos, canvas.trace_color)

    def change_n(self, amount):
        self.color_shift = self.time
        if self.n + amount > 0:
            self.n += amount
        self.calculate_coeficients()
        self.draw_last_line = False
        self.aprox_trace = []

    def change_zoom(self, amount):
        if self.zoom + amount > 0:
            self.zoom += amount

    def reset(self):
        self.trace = []
        self.aprox_trace = []
        self.coefficients = []
        self.time = 0
        self.zoom = 1
        self.draw_last_line = False
        self.toggle_circles = True
        self.toggle_lines = True
        self.toggle_points = True


def extract_svg():
    attributes, svg_attributes = svgpathtools.svg2paths2(args.input_file)[1:]
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
                ft.trace.append((complex_point.real/image_w*canvas.width - canvas.width//2,
                                complex_point.imag/image_h*canvas.height - canvas.height//2))

def hold_arrows():
    for arr in arrows:
        time_now = time.monotonic() 
        if arr["hold"] and time_now - arr["press_time"] > REPEAT_AFTER:
            arr["press_time"] = time_now
            if arr['key'] in [pygame.K_UP, pygame.K_DOWN]:
                arr['action'](arr['amount'])
            elif ft.n + arr['delta'] + arr['amount'] > 0:
                arr['delta'] += arr['amount']
        elif arr["press_time"] > 0 and time_now - arr["press_time"] > HOLD_AFTER:
            arr['hold'] = True
        

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-r', '--resolution', nargs=2,
                        help='set width and height of the window, default is fullscreen')
arg_parser.add_argument('-i', '--input-file', type=str,
                        help='specify a .svg file for trace')
arg_parser.add_argument('-n', '--num-of-functions', type=int,
                        default=100, help='number of functions used to approximate the curve')
arg_parser.add_argument('-s', '--sampling-rate', type=int,
                        default=50, help='mark trace of curve every n miliseconds')
arg_parser.add_argument('-u', '--update-rate', type=int, default=50,
                        help='one frame will take n miliseconds')
arg_parser.add_argument('-d', '--point-density', type=int,
                        default=200, help='number of point samples per path')
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
HOLD_AFTER = 0.5  # hold the zoom keys after n seconds
REPEAT_AFTER = 0.01

if args.input_file:
    extract_svg()
    ft.calculate_coeficients()
    STATE = 2  # trace is recorded skip 1 state
else:
    canvas.draw_grid()
    canvas.print_welcome_text()
    pygame.display.update()


prev_time, current_time = 0, 0
arrows = [{"key": pygame.K_UP, "press_time": -1, "hold": False,
          "action": ft.change_zoom, "amount": 0.04, "delta": 0},
          {"key": pygame.K_DOWN, "press_time": -1, "hold": False,
          "action": ft.change_zoom, "amount": -0.04, "delta": 0},
          {"key": pygame.K_RIGHT, "press_time": -1, "hold": False,
          "action": ft.change_n, "amount": 1, "delta": 0},
          {"key": pygame.K_LEFT, "press_time": -1, "hold": False,
          "action": ft.change_n, "amount": -1, "delta": 0}]


while True:
    current_time = time.monotonic()
    # catch events
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                sys.exit()
            if e.key == pygame.K_SPACE and STATE < 2:
                canvas.display.fill(canvas.bg_color)
                if STATE == 0:
                    canvas.draw_grid()
                    ft.trace = [pygame.mouse.get_pos()]
                    prev_time = current_time
                if STATE == 1:
                    ft.calculate_coeficients()
                STATE += 1
            if e.key == pygame.K_r:
                STATE = 0
                canvas.reset()
                ft.reset()
            if e.key == pygame.K_p:
                ft.toggle_points = not ft.toggle_points
            if e.key == pygame.K_l:
                ft.toggle_lines = not ft.toggle_lines
            if e.key == pygame.K_c:
                ft.toggle_circles = not ft.toggle_circles
            for arr in arrows:
                if e.key == arr["key"] and STATE == 2:
                    arr['action'](arr['amount'])
                    arr['press_time'] = current_time
        elif e.type == pygame.KEYUP:
            for arr in arrows:
                if e.key == arr["key"] and STATE == 2:
                    arr["press_time"] = -1
                    arr['action'](arr['delta'])
                    arr['delta'] = 0
                    arr['hold'] = False
    hold_arrows()

    # drawing points
    if STATE == 1 and current_time - prev_time >= SAMPLE_RATE:
        prev_time = current_time
        ft.record_point()

    # run animation
    if STATE == 2 and current_time - prev_time >= UPDATE_RATE:
        prev_time = current_time
        canvas.display.fill(canvas.bg_color)
        ft.calculate_point()
        ft.draw_curve()
        canvas.print_stats(ft.zoom, ft.n)

    pygame.display.update()
