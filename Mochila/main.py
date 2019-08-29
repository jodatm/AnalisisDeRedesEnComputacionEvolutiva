  
import random
from item import Item

##########################################################################################
# Codigo del Problema de la mochila tomado de: https://github.com/edmilsonrobson 
##########################################################################################
# 

ITEMS = [Item(random.randint(0,30),random.randint(0,30)) for x in range (0,30)]

CAPACITY = 10*len(ITEMS)

POP_SIZE = 50

GEN_MAX = 200

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
        return [random.randint(0,0) for x in range (0,len(ITEMS))]
    else:
        return [random.randint(0,1) for x in range (0,len(ITEMS))]

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
    for g in range(0,GEN_MAX):        
        population = sorted(population, key=lambda x: fitness(x), reverse=True)        
        population = evolve_population(population)
        fitness_generations.append(fitness(population[0]))
        generation += 1
    return fitness_generations

if __name__ == "__main__":
    number_experiments = 100
    promedios = []
    experiments = []
    for i in range (0,number_experiments):
        experiments.append(main())        
    
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
        
    
