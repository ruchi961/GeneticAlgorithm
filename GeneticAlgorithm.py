from random import choices
from random import randrange
from random import uniform
genes = ["I","N","D","A"]
targetString =["I","N","D","I","A"]
initalPopulation=[]
n=4
iterations=0
#creating initial random population
def create_randomPopulation():
    global genes, initalPopulation,n
    for i in range(n):
        #random.choices(genes)
        while True:
            random_choices = []
            for i in range(5):
                random_choices.append(randrange(0,4))
            if random_choices.count(0) >=2 and random_choices.count(1) >=1 and random_choices.count(2) >=1 and random_choices.count(3) >=1:
                break
        individual=[]
        for i in range(len(random_choices)):
            individual.append(genes[random_choices[i]])
        initalPopulation.append(individual)
def determineFitness(population):
    #target string is INDIA
    global targetString
    print("popie",population)
    fitness_list=[]
    probability_list=[]
    for i in population:
        fitness=0
        for j in range(len(i)):
            if targetString[j] == i[j]:
                fitness+=1
        fitness_list.append(fitness)
    denominator = sum(fitness_list)
##    if denominator ==0:
##        for i in range(len(fitness_list)):
##            fitness_list[i]=-1
##        denominator = sum(fitness_list)
            
    print("Fitness of the population is : ",fitness_list)
    for i in range(len(fitness_list)):
        probability_list.append(fitness_list[i]/denominator)
    
    print("Probability of the population is : ",probability_list)
    return(fitness_list,probability_list)




   
##def crossover(parents):
##    print("parentsdgdfgdffd",parents)
##    random_crosspoint = randrange(0,len(parents[0]))
##    offspring1=[]
##    for i in range(random_crosspoint):
####        if i==random_crosspoint:
####            break
##        offspring1.append(parents[0][i])
##    for i in range(0,len(parents[1])):
##        if len(offspring1)==5:
##            break
##        print("oofspring1",offspring1,parents[1][i] in offspring1,parents[1][i],random_crosspoint)
##        if parents[1][i] in offspring1:
##            #need two Is
##            if parents[1][i] =="I":
##                #print("count",offspring1.count("I"))
##                if offspring1.count("I")<2:
##                    offspring1.append(parents[1][i])
##        else:
##            offspring1.append(parents[1][i])
##
##    offspring2=[]
##    for i in range(random_crosspoint):
####        if i==random_crosspoint:
####            break
##        offspring2.append(parents[1][i])
##    for i in range(0,len(parents[0])):
##        if len(offspring2)==5:
##            break
##        print("oofspring2",offspring2,parents[0][i] in offspring2,parents[0][i],random_crosspoint)
##        if parents[0][i] in offspring2:
##            if parents[0][i] =="I":
##                #need two Is
##                if offspring2.count("I")<2:
##                    offspring2.append(parents[0][i])
##        else:
##            offspring2.append(parents[0][i])
##    print("offspring from crosso over is : ",offspring1,offspring2)
##    return offspring1,offspring2





##def crossover(parents):
##    print("parentsdgdfgdffd",parents)
##    random_crosspoint=[]
##    while True:
##            randomPoint= randrange(0,len(parents[0]))
##            if randomPoint not in random_crosspoint:
##                random_crosspoint.append(randomPoint)
##            if len(random_crosspoint)==3:
##                break
##    offspring1=[]
##
##    for i in range(0,len(parents[0])):           
##            offspring1.append(parents[0][i])
##    for i in random_crosspoint:          
##            offspring1[i] = parents[1][i]        
##
##    offspring2=[]
##
##    for i in range(0,len(parents[1])):           
##            offspring2.append(parents[1][i])
##    for i in random_crosspoint:          
##            offspring2[i] = parents[0][i]         
##
##    print("offspring from crosso over is : ",offspring1,offspring2)
##    return offspring1,offspring2


##def mutations(population):
##    random_mutationpoint1 = randrange(0,len(population[0]))
##    random_mutationpoint2 = randrange(0,len(population[0]))
##    print("random",random_mutationpoint2,random_mutationpoint1)
##    for i in range(len(population)):
##        temp = population[i][random_mutationpoint1]
##        population[i][random_mutationpoint1] = population[i][random_mutationpoint2]
##        population[i][random_mutationpoint2]= temp
##    #print("Mutations population is : ",population)
##    return population

def mutation():
    global genes
    random_mutationpoint1 = randrange(0,len(genes))
    return genes[random_mutationpoint1]

def crossover(parents):
    print("parentsdgdfgdffd",parents)
    offspring1=[]
    offspring2=[]
    for i in range(len(parents[0])):
            randomPoint= uniform(0,1)
            if randomPoint<=0.9:
                #perform crossover as its probability is high
                #unifrom crossover
                if randomPoint<=0.45:
                    #for first offspring
                    offspring1.append(parents[0][i])
                    #for second offspring
                    offspring2.append(parents[1][i])
                else:
                    offspring1.append(parents[1][i])
                    #for second offspring
                    offspring2.append(parents[0][i])
                
            else:
                offspring1.append(mutation())
                offspring2.append(mutation())
                    
                
    print("offspring from crosso over is : ",offspring1,offspring2)
    return offspring1,offspring2


##def mutations(population):
##    while True:
##        random_mutationpoint1 = randrange(0,len(population[0]))
##        random_mutationpoint2 = randrange(0,len(population[0]))
##        if random_mutationpoint1 != random_mutationpoint2:
##            break
##    print("random",random_mutationpoint2,random_mutationpoint1)
##    #for i in range(len(population[0])):
##    temp = population[0][random_mutationpoint1]
##    population[0][random_mutationpoint1] = population[1][random_mutationpoint2]
##    population[1][random_mutationpoint2]= temp
##    print("Mutations population is : ",population)
##    return population[0],population[1]


    
def roulettesFunction(population):
    global iterations
    print("iteration : ",iterations)
    global n
    fitness_list=[]
    probability_list=[]
    new_population=[]
    fitness_list,probability_list = determineFitness(population)
    #for i in range(int(n/2)):
    parents = choices(population,weights=probability_list,k=n)
    print("Parents are : ",parents)
    offspring1,offspring2 = crossover(parents[0:2])
##    if offspring1 == offspring2:
##        offspring1,offspring2 = mutations([offspring1,offspring2])
       
    new_population.append(offspring1)
    new_population.append(offspring2)
    offspring1,offspring2 = crossover(parents[2:4])
##    if offspring1 == offspring2:
##        offspring1,offspring2 = mutations([offspring1,offspring2])

    new_population.append(offspring1)
    new_population.append(offspring2)

    print("The new Selected population after crossover is : ",new_population)
    
    #print("The new Selected population after mutation is : ",new_population)
    if targetString in new_population:
            print("Target string : INDIA found")
            return
    iterations+=1
    roulettesFunction(new_population)
    return
    #crossover(new_population)


create_randomPopulation()
print("Initial population is : ",initalPopulation)
roulettesFunction(initalPopulation)
