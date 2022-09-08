#!/usr/bin/python

from svgpathtools import svg2paths2
from svgpathtools import parse_path
import pygame

paths, attributes, svg_attributes = svg2paths2('sample_svg/sample5.svg')

w = 600
h = 300                
wim = int(float(svg_attributes['width'].replace('mm', ''))*100)
him = int(float(svg_attributes['height'].replace('mm', ''))*100)

pygame.init()                  
surface = pygame.display.set_mode((w,h)) # get surface to draw on
surface.fill(pygame.Color('white'))  # set background to white

scaled_points = []
for idx, attr in enumerate(attributes):
    if attr.get('d') and attr.get('stroke'):
        svgpath = attr['d']

        path = parse_path(svgpath)
        n = 100  # number of line segments to draw
        pts = []
        for i in range(0,n+1):
            f = i/n  # will go from 0.0 to 1.0
            complex_point = path.point(f)  # path.point(t) returns point at 0.0 <= f <= 1.0
            pts.append((complex_point.real/wim*w, complex_point.imag/him*h))
        pygame.draw.aalines( surface,pygame.Color('blue'), False, pts)  # False is no closing
        scaled_points.append(pts)
pygame.display.update() # copy surface to display


while True:  # loop to wait till window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()