#!/usr/bin/python

import numpy as np
import random
import copy
import matplotlib.pyplot as plt


def fitness(individual):
    # set the fitness as the sum of all costs, but if
    # it exceeds capacity it will be negative value
    N = len(individual)
    value, total_weight = 0, 0
    for i in range(N):
        value += individual[i]*items[i][0]
        total_weight += individual[i]*items[i][1]
    if total_weight >= K: return K - total_weight
    else: return value


def random_population(population_size, individual_size):
    # create random list of bits
    population = []
    for i in range(0,population_size):
        individual = np.random.choice([0, 1], size=individual_size)
        population.append(individual)
    return population


def crossover_mean(population, cross_prob=0.75):
    # classic crossover with randomly chosen point
    new_population = []
    for j in range(0,len(population)//2):
        indiv1 = copy.deepcopy(population[2*j])
        indiv2 = copy.deepcopy(population[2*j+1])
        child1 = indiv1
        child2 = indiv2
        if random.random()<cross_prob:
            point = np.random.randint(len(indiv1))
            for i in range(len(child1)): 
                if i < point: child1[i] = indiv2[i] 
                else: child2[i] = indiv1[i]
        new_population.append(child1)
        new_population.append(child2)
    return new_population


def mutation_switch(population,individual_mutation_prob=1/3,value_mutation_prob=1/(1000/6)):
    # perform classic mutation by switching bits
    new_population = []
    for j in range(len(population)):
        individual = copy.deepcopy(population[j])
        if random.random() < individual_mutation_prob:
            for i in range(len(individual)):
                if random.random() < value_mutation_prob:
                    individual[i] = abs(individual[i]-1)
        new_population.append(individual)
    return new_population


def selection(population,fitness_value, M): 
    # strategy is to choose the best individual 
    # from M randomly selected ones
    new_population = []
    for i in range(len(population)):
        individuals, fit = [], []
        for _ in range(M):
            idx = random.randint(0,len(population)-1)
            individuals.append(population[idx])
            fit.append(fitness_value[idx])
        new_population.append(copy.deepcopy(individuals[np.argmax(fit)]))
    return new_population 


def evolution(population_size, individual_size, max_generations):
    max_fitness, population = [], random_population(population_size,individual_size)
    for i in range(max_generations):
        fitness_value = list(map(fitness, population))
        max_fitness.append(max(fitness_value))
        parents = selection(population, fitness_value, 20)
        children = crossover_mean(parents)
        mutated_children = mutation_switch(children)
        population = mutated_children
        if i % 10 == 0: print(i, max_fitness[-1])

    max_fitness.append(max(list(map(fitness, population))))
    # best_individual = population[np.argmax(fitness_value)]
    return max_fitness



# input_file = "debugging_data_20.txt"
input_file = "input_data_100.txt"

items = []
with open(input_file, 'r') as inp:
    N, K = [int(i) for i in inp.readline().split(' ')]
    
    for _ in range(N):
        cost, weight = [int(i) for i in inp.readline().split(' ')]
        items.append([cost, weight])

max_fitness = evolution(population_size=N*4, individual_size=N, max_generations=250)
print("done")
print("-"*30)
print('best fitness: ', max(max_fitness))

plt.plot(max_fitness)
plt.ylabel('Fitness')
plt.xlabel('Generations')
plt.show()
