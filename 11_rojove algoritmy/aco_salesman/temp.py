import re
import xml.etree.ElementTree as ET
from collections import namedtuple
import numpy as np
import functools
import pprint
import math
import csv

from matplotlib import collections as mc
import matplotlib.pyplot as plt


@functools.lru_cache(maxsize=None)
def distance(v1, v2):
    return math.sqrt((v1.x - v2.x)**2+(v1.y - v2.y)**2)

def fitness(vertices, distance, solution):
    solution_distance = 0
    for x, y in zip(solution, solution[1:]):
        solution_distance += distance(vertices[x], vertices[y])
    solution_distance += distance(vertices[solution[-1]], vertices[solution[0]])
    return solution_distance

def initialize_pheromone(N):
    return 0.01*np.ones(shape=(N,N))

def update_pheromone(pheromones_array, solutions, fits, Q=100, rho=0.6):
    pheromone_update = np.zeros(shape=pheromones_array.shape)
    for solution, fit in zip(solutions, fits):
        for x, y in zip(solution, solution[1:]):
            pheromone_update[x][y] += Q/fit
        pheromone_update[solution[-1]][solution[0]] += Q/fit
    return (1-rho)*pheromones_array + pheromone_update


def generate_solutions(vertices, vehicle_capacity, warehouse_id, pheromones, distance, N, alpha=1, beta=3):
    
    # pravdepodobnost vyberu dalsiho mesta
    def compute_prob(v1, v2):
        dist = 1/distance(vertices[v1], vertices[v2])
        tau = pheromones[v1, v2]
        ret = pow(tau, alpha) * pow(dist,beta)
        return ret if ret > 0.000001 else 0.000001

    pheromones_shape = pheromones.shape[0]
    for i in range(N):
        available = list(range(pheromones_shape))
        
        solution = [warehouse_id]
        vehicle_load = 0
        vehicle_quanity = 1
        path = [warehouse_id]
        
        available.remove(solution[0])

        while available:
            probs = np.array(list(map(lambda x: compute_prob(path[-1], x), available)))
            selected = np.random.choice(available, p=probs/sum(probs)) # vyber hrany
            vehicle_load += vertices[selected][2]

            if vehicle_load <= vehicle_capacity:
                available.remove(selected)
                path.append(selected)
            else:
                solution += path[1:]
                vehicle_load = 0
                vehicle_quanity += 1
                path = [warehouse_id]
        
        if len(path) > 1: 
            solution += path[1:]
            vehicle_quanity += 1
        solution.append(vehicle_quanity)
        yield solution


def format_solution(solutions):
    path, vehicles = [], []
    for s in solutions:
        v = s.pop()
        vehicles.append(v)
        path.append(s)
    return path, vehicles


def format_fitness(fits):
    distance, fitness = [], []
    for f in fits:
        distance.append(f[0])
        fitness.append(f[1])
    return fitness, distance


def ant_solver(vertices, vehicle_capacity, warehouse_id, distance, ants=10, max_iterations=20, alpha=1, beta=3, Q=100, rho=0.8):
    pheromones = initialize_pheromone(len(vertices))
    best_solution = None
    best_fitness = float('inf')
    
    for i in range(max_iterations):
        # last number in solutions contains number of vehicles used
        solutions = list(generate_solutions(vertices, vehicle_capacity, warehouse_id, pheromones, distance, ants, alpha=alpha, beta=beta))
        path, vehicles = format_solution(solutions)

        fits = list(map(lambda x: fitness(vertices, distance, x), path))
        # fitt, distance = format_fitness(fits)
        pheromones = update_pheromone(pheromones, path, fits, Q=Q, rho=rho)
        
        for s, f in zip(path, fits):
            if f < best_fitness:
                best_fitness = f
                best_solution = s
        
        print(f'{i:4}, {np.min(fits):.4f}, {np.mean(fits):.4f}, {np.max(fits):.4f}')
    return best_solution, pheromones


# ---------------------------------------------------------------------------------------------


test = "data_32.xml"
# test = "data_72.xml"
# test = "data_422.xml"
tree = ET.parse(f"data/{test}")
root = tree.getroot()

cat = {"info": 0, "network": 1, "fleet": 2, "requests": 3}  # categories
Vertex = namedtuple('Vertex', ['name', 'x', 'y', 'size'])


# fleet info
vehicle_capacity = -1
for fleet in root[cat["fleet"]]: vehicle_capacity = float(fleet[2].text)

# graph
coords = {}
vertices = []
warehouse_id = 0
for nodes in root[cat["network"]]:
    for node in nodes:
        if int(node.attrib["type"]) == 0: vertices.append(Vertex(int(node.attrib['id']), float(node[0].text), float(node[1].text), 0))
        coords[int(node.attrib['id'])] = [float(node[0].text), float(node[1].text), int(node.attrib["type"])]

# requests
for req in root[cat["requests"]]:
    id = int(req.attrib["node"])
    # if coords[id][2] == 0: warehouse_id = len(vertices)
    vertices.append(Vertex(id, coords[id][0], coords[id][1], float(req[0].text)))

# vertices = []
# with open('cities.csv') as cities_file:
#     csv_reader = csv.reader(cities_file, delimiter=',')
#     for row in csv_reader:
#         vertices.append(Vertex(row[0], float(row[2]), float(row[1])))


best_solution, pheromones = ant_solver(vertices, vehicle_capacity, warehouse_id, distance)


lines = []
colors = []
for i, v1 in enumerate(vertices):
    for j, v2 in enumerate(vertices):
        lines.append([(v1.x, v1.y), (v2.x, v2.y)])
        colors.append(pheromones[i][j])

lc = mc.LineCollection(lines, linewidths=np.array(colors))

plt.figure(figsize=(12, 8))
ax = plt.gca()
ax.add_collection(lc)
ax.autoscale()

solution = best_solution

# tady muzeme zkouset vliv jednotlivych parametru na vygenerovane reseni
# solution = list(generate_solutions(vertices, pheromones, distance, N=1, alpha=3, beta=1))[0]

print('Fitness: ', fitness(vertices, distance, solution))

solution_vertices = [vertices[i] for i in solution]
# pprint.pprint(solution_vertices)

solution_lines = []
for i, j in zip(solution, solution[1:]):
    solution_lines.append([(vertices[i].x, vertices[i].y), (vertices[j].x, vertices[j].y)])
solution_lines.append([(vertices[solution[-1]].x, vertices[solution[-1]].y), (vertices[solution[0]].x, vertices[solution[0]].y)])
solutions_lc = mc.LineCollection(solution_lines, colors='red')
ax.add_collection(solutions_lc)

plt.show()