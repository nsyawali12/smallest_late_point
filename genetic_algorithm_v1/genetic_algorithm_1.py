from genetic_algorithm_v1.dataset_input_0 import place_name, matrix_distances
import random
from random import randint

def create_population(size, genes):
    population = []

    for _i in range(size):
        chromosome = random.sample(genes, len(genes))
        population.append(chromosome)
    
    return population

def calculate_fitness(chromosome, distance_matrix):
    fitness = 0
    for i in range(len(chromosome)-1):
        start = chromosome[i]
        end = chromosome[i+1]
        fitness += distance_matrix(start, end)
    
    return fitness

def calculate_distances_times(route_sequences, time_matrix):
    distances = []
    for sequence in route_sequences:
        route_distances = []
        for i in range(len(sequence) - 1):
            start = int(sequence[i])
            end = int(sequence[i + 1])
            distance = time_matrix[start][end]
            route_distances.append(distance)
        distances.append(route_distances)
    return distances

def selection(population, distance_matrix):
    parents = random.sample(population, 2)
    fitness_parent1 = calculate_fitness(parents[0], distance_matrix)
    fitness_parent2 = calculate_fitness(parents[1], distance_matrix)
    return min(parents, key=lambda x: calculate_fitness(x, distance_matrix))

def crossover(parent1, parent2):
    child = [-1] * len(parent1)
    start = random.randint(0, len(parent1) - 1)
    end = random.randint(0, len(parent1) - 1)

    if start > end:
        start, end = end, start

    for i in range(start, end + 1):
        child[i] = parent1[i]

    j = 0
    for i in range(len(parent2)):
        if child[i] == -1:
            while parent2[j] in child:
                j += 1
            child[i] = parent2[j]
    
    return child

def mutation(chromosome):
    index1 = random.randint(0, len(chromosome) - 1)
    index2 = random.randint(0, len(chromosome) - 1)
    chromosome[index1], chromosome[index2] = chromosome[index2], chromosome[index1]
    return chromosome

def genetic_algorithm(distance_matrix, genes, fitness_function, population_size=10, generations=25):
    population = create_population(population_size, genes)

    for _g in range(generations):
        new_population = []

        while len(new_population) < population_size:
            parent1 = selection(population, distance_matrix)
            parent2 = selection(population, distance_matrix)

            child = crossover(parent1, parent2)

            if random.random() < 0.1:
                child = mutation(child)
            
            new_population.append(child)
        
        population = new_population
    
    best_chromosome = min(population, key=lambda x: fitness_function(x, distance_matrix))
    best_fitness = fitness_function(best_chromosome, distance_matrix)
    return best_chromosome, best_fitness