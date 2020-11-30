#Author: Joshua David Triana
#Creation date Agosto 29 de 2019
#Last edition date Agosto 29 de 2019
#Description: Backpack function experiments    
import random
from item import Item
import numpy as np
import time
##########################################################################################
# Codigo del Problema de la mochila tomado de: https://github.com/edmilsonrobson 
##########################################################################################
# 
number_items = 80
ITEMS = [Item(random.randint(0,number_items),random.randint(0,number_items)) for x in range (0,number_items)]

CAPACITY = 10*len(ITEMS)

POP_SIZE = 50

GEN_MAX = 100

START_POP_WITH_ZEROES = False


def fitness(target):    
    total_value = 0
    total_weight = 0
    index = 0
    for i in target:        
        if index >= len(ITEMS):
            break
        if (i == 1):
            total_value += ITEMS[index].value
            total_weight += ITEMS[index].weight
        index += 1
        
    
    if total_weight > CAPACITY:
        return 0
    else:
        return total_value

def spawn_starting_population(amount):
    return [spawn_individual() for x in range (0,amount)]

def spawn_individual():
    if START_POP_WITH_ZEROES:
        return [0 for x in range (0,len(ITEMS))]
    else:
		capacityInd = 0
		individual = np.zeros( len(ITEMS))
		individual = individual.tolist()
		for i in range(0, len(ITEMS)):
			status = random.randint(0,1) 
			if status == 1:
				if capacityInd + ITEMS[i].weight <= CAPACITY:
					individual[i] = status
					capacityInd = capacityInd + ITEMS[i].weight
				else:
					return individual
        #[random.randint(0,1) for x in range (0,len(ITEMS))]
		return individual

def mutate(target):    
    r = random.randint(0,len(target)-1)
    if target[r] == 1:
        target[r] = 0
    else:
        target[r] = 1

def evolve_population(pop):
    parent_eligibility = 0.2
    mutation_chance = 0.08
    parent_lottery = 0.05

    parent_length = int(parent_eligibility*len(pop))
    parents = pop[:parent_length]
    nonparents = pop[parent_length:]

    # Parent lottery!
    for np in nonparents:
        if parent_lottery > random.random():
            parents.append(np)

    # Mutation lottery... I guess?
    for p in parents:
        if mutation_chance > random.random():
            mutate(p)

    # Breeding! Close the doors, please.
    children = []
    desired_length = len(pop) - len(parents)
    while len(children) < desired_length :
        male = pop[random.randint(0,len(parents)-1)]
        female = pop[random.randint(0,len(parents)-1)]        
        half = len(male)/2
        child = male[:half] + female[half:] # from start to half from father, from half to end from mother
        if mutation_chance > random.random():
            mutate(child)
        children.append(child)

    parents.extend(children)
    return parents


def main():
    generation = 0
    population = spawn_starting_population(POP_SIZE)

    fitness_generations = []
    start_time = time.time()
    times = []
 
    for g in range(0,GEN_MAX):
        population = evolve_population(population)
        times.append(time.time() - start_time)  
        fitness_mas_alto = 0
        
        for i in range (0,len(population)):
            if fitness(population[i])>fitness_mas_alto:
                fitness_mas_alto = fitness(population[i])
        
        fitness_generations.append(fitness_mas_alto)
        generation += 1
    return fitness_generations,times

if __name__ == "__main__":
    number_experiments = 100
    promedios = []
    experiments = []
    timess = []

    for i in range (0,number_experiments):
		print("experiments: ",i)
		response = main()
		experiments.append(response[0])
		timess.append(response[1])
    
    for i in range(0,GEN_MAX):
        sumatoria_temporal = 0
        for j in range(0,number_experiments):
            sumatoria_temporal = sumatoria_temporal + experiments[j][i]
        

        promedio_temporal = sumatoria_temporal / number_experiments        
        promedios.append(promedio_temporal)
    
    print("\n")
    print("Promedios de las iteraciones")
    for i in range(0,GEN_MAX):
        #print(promedios[i])
        print str(promedios[i]),
        
    average_times = np.average(timess,axis=0)
    print(average_times)       


        
    
