import random
import math
import networkx as nx
#import time

#temps1 = time.time()

def func1(x):
    c=2*math.pi    
    res1=math.sqrt(0.5*((x[0]**2)+(x[1]**2)))
    sum1 = -20*math.exp(-0.2*(res1))    
    res2=0.5*(math.cos(c*x[0])+math.cos(c*x[1]))
    sum2 = -math.exp(res2)    
    resultado =sum1 + sum2+ math.e + 20        
    return resultado

def ensure_bounds(vec, bounds):

    vec_new = []
    # cycle through each variable in vector 
    for i in range(len(vec)):

        # variable exceedes the minimum boundary
        if vec[i] < bounds[i][0]:
            vec_new.append(bounds[i][0])

        # variable exceedes the maximum boundary
        if vec[i] > bounds[i][1]:
            vec_new.append(bounds[i][1])

        # the variable is fine
        if bounds[i][0] <= vec[i] <= bounds[i][1]:
            vec_new.append(vec[i])
        
    return vec_new
#    
cost_func = func1                   # Cost function
bounds = [(-5,5),(-5,5)]            # Bounds [(x1_min, x1_max), (x2_min, x2_max),...]
popsize = 100                       # Population size, must be >= 4
mutate = 0.1                        # Mutation factor [0,2]
rewiring = 0.3                      # Rewiring probability [0,1]
maxiter = 50                        # Max number of generations (maxiter)


def main(cost_func, bounds, popsize, mutate, rewiring, maxiter):
    G = nx.generators.random_graphs.watts_strogatz_graph(popsize,3,rewiring)        
    
    population = []
    for i in range(0,popsize):
        indv = []
        for j in range(len(bounds)):
            indv.append(random.uniform(bounds[j][0],bounds[j][1]))
        population.append(indv)
    scores = []    
    
    for l in range(0,maxiter):            
        gen_scores=[]    
        for j in range(0, popsize):        
            candidato = population[j]            
            vecinos=[]
            for k in G[j]:
                vecinos.append(k)
                
            if(len(vecinos)>0):            
                random_index = random.sample(vecinos, 1)                                        
                pareja = population[random_index[0]]                
                child = []
                
                for i in range(len(candidato)):
                    if (int(100 * random.random()) < 50):
                        child.append(candidato[i])
                    else:
                        child.append(pareja[i])
                        
                for i in range(len(bounds)):
                    if random.random() < mutate:                         
                         child[i] = random.uniform(bounds[i][0],bounds[i][1])                            
                         
                score_individuo  = cost_func(candidato)
                score_child = cost_func(child)
                
                if(score_child < score_individuo):                    
                    population[j] =  child                    
                    G.add_edge(j,random_index[0])
                    gen_scores.append(score_child)
                gen_scores.append(score_individuo)
                
        for j in range(0, popsize):            
            aristas = G.adj[j]            
            
            vecinos=[]
            for k in aristas:                
                vecinos.append(k)
                                    
            for i in range(0,len(vecinos)):
                if random.random() < rewiring:                    
                    random_index = int(random.random()*100)                    
                    G.remove_edge(j, vecinos[i])                    
                    G.add_edge(j,random_index)
                    
        gen_best = min(gen_scores)        
        scores.append(gen_best)        
    
    return scores
    
iteraciones = []      
promedios = []

numero_iteraciones = 100

for i in range(0,numero_iteraciones):
    print(i)
    iteracionTemporal = main(cost_func, bounds, popsize, mutate, rewiring, maxiter)
    iteraciones.append(iteracionTemporal)
    
for i in range(0,maxiter):
    sumatoria_temporal = 0
    for j in range(0,numero_iteraciones):        
        sumatoria_temporal = sumatoria_temporal + iteraciones[j][i]
            
    promedio_temporal = sumatoria_temporal / numero_iteraciones
    promedios.append(promedio_temporal)
    
print("\n")
print("Promedios de las iteraciones")
for i in range(0,maxiter):    
    print("%.9f"%promedios[i], end=';')   
    
#print(time.time() - temps1)