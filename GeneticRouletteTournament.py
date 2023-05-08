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
        random_choices = []
        for i in range(5):
            random_choices.append(randrange(0,4))
##        while True:
##            random_choices = []
##            for i in range(5):
##                random_choices.append(randrange(0,4))
##            if random_choices.count(0) >=2 and random_choices.count(1) >=1 and random_choices.count(2) >=1 and random_choices.count(3) >=1:
##                break
        individual=[]
        for i in range(len(random_choices)):
            individual.append(genes[random_choices[i]])
        initalPopulation.append(individual)

def determineFitness(population):
    #target string is INDIA
    global targetString
    print("Finding fitness and probability values for the population : ",population)
    fitness_list=[]
    probability_list=[]
    
    for i in population:
        #fitnes value of each individual n population
        fitness=0
        for j in range(len(i)):
            #checking if the nidivual in the population matches with the target String
            #how much characters match at exact position
            #we have to maximize the fitnesss function
            #i.e. individuals having comparatively big fitness values are fitter parents
            #as they close to the target string in terms of position of characters
            if targetString[j] == i[j]:
                fitness+=1
        fitness_list.append(fitness)

    #the fitness value of the population
    print("Fitness of the population is : ",fitness_list)
    
    #finding the sum of the fitness values
    denominator = sum(fitness_list)
    #finding the probabiity of the population's fitness
    for i in range(len(fitness_list)):
        probability_list.append(fitness_list[i]/denominator)
    
    print("Probability of the population is : ",probability_list)
    #return fitness and probability list values
    return(fitness_list,probability_list)


def mutation():
    #performing unifrom mutation
    global genes
    #find a random point for mutation and return the value from [I,N,D,A] which is the range of values
    #for the string to generate    
    random_mutationpoint1 = randrange(0,len(genes))
    return genes[random_mutationpoint1]

def crossover(parents):
    print("Parents for crossover are: ",parents)
    offspring1=[]
    offspring2=[]
    print("Generating offsprings...")
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
                print("crossover perforomed: offspring1: ",offspring1,"offspring2: ",offspring2)
                
            else:
                offspring1.append(mutation())
                offspring2.append(mutation())
                print("mutation perforomed: offspring1: ",offspring1,"offspring2: ",offspring2)
                    
                
    print("offsprings from crossover and mutation of parents are : ",offspring1,offspring2,"\n")
    return offspring1,offspring2


    
def roulettesFunction(population):
    global iterations, n
    print("".center(90,"*"))
    print("Iteration (Generation) : ",iterations)
    print("".center(90,"*"))

    fitness_list=[]
    probability_list=[]
    new_population=[]
    #find the fitness and probability of the population
    fitness_list,probability_list = determineFitness(population)

    #using roulettes wheel to select fit population as parents
    #here 4 fittest parents are choosen and divided into half for next population
    parents = choices(population,weights=probability_list,k=n)
    #print parets
    print("Fittest Parents selected with roulettes wheel from the population are : ",parents)
    val = sum(fitness_list)
    
    print("\nGeneration new offsprings..........")

    #first two offsprings
    offspring1,offspring2 = crossover(parents[0:2])

    #Creating their new population       
    new_population.append(offspring1)
    new_population.append(offspring2)

    #another two offsprings
    offspring1,offspring2 = crossover(parents[2:4])
    #appending them to new population 
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    print("The new generation after crossover and mutation is : ",new_population)

    #base condition of recursion
    if targetString in new_population:
        print("".center(90,"*"))
        print("Target string : INDIA found after ",iterations," iterations (Generations).")
        print("".center(90,"*"))
        return
    else:
        print("\nTarget String not found...........")

    #going for next generation
    iterations+=1
    print("".center(90,"*"))
    print("checking new generation's fitness to deciede whether to change the selection function or not....") 
    fitness_list,probability_list = determineFitness(new_population)
    print("Total Fitness of he old poplation : ", val)
    print("Total fitness of the new poppulaton is : ",sum(fitness_list))
    if val > sum(fitness_list):
        print("".center(90,"*"))
        print("Fitness dropped, going for tournament selection method")
        print("".center(90,"*"))
        tournamentFunction(new_population)
    else:
        print("".center(90,"*"))
        print("Fitness increased, continuing with roulette selection method")
        print("".center(90,"*"))
        roulettesFunction(new_population)
    #to return recursively
    return



def tournamentFunction(population):
    global iterations, n
    print("".center(90,"*"))
    print("Iteration (Generation) : ",iterations)
    print("".center(90,"*"))

    fitness_list=[]
    probability_list=[]
    new_population=[]
    #find the fitness and probability of the population
    fitness_list,probability_list = determineFitness(population)
    parents=[]
    #using tournament selection to select fit population as parents
    #choose parents loop
    for i in range(4):
        #find 2 random positions for 2 way tournament
        random_list=[]
        for i in range(2):
            random_list.append(randrange(0,len(population[0])-1))
        print(random_list)
        #find their fitness score
        fitnessChoose=[]
        for i in random_list:
            fitnessChoose.append(fitness_list[i])
        #indivudal with maximum fitness will be selected as parent
        value = max(fitnessChoose)
        index = fitness_list.index(value)
        parents.append(population[index])
    
    #print parents
    print("Fittest Parents selected with roulettes wheel from the population are : ",parents)
    val = sum(fitness_list)
    
    print("\nGeneration new offsprings..........")

    #first two offsprings
    offspring1,offspring2 = crossover(parents[0:2])

    #Creating their new population       
    new_population.append(offspring1)
    new_population.append(offspring2)

    #another two offsprings
    offspring1,offspring2 = crossover(parents[2:4])
    #appending them to new population 
    new_population.append(offspring1)
    new_population.append(offspring2)
    
    print("The new generation after crossover and mutation is : ",new_population)

    #base condition of recursion
    if targetString in new_population:
        print("".center(90,"*"))
        print("Target string : INDIA found after ",iterations," iterations (Generations).")
        print("".center(90,"*"))
        return
    else:
        print("\nTarget String not found...........")

    #going for next generation
    iterations+=1
    print("".center(90,"*"))
    
    
    #tournamentFunction(new_population)
    #roulettesFunction(new_population)
    #to return recursively
    print("checking new generation's fitness to deciede whether to change the selection function or not....") 
    fitness_list,probability_list = determineFitness(new_population)
    print("Total Fitness of the old poplation : ", val)
    print("Total fitness of the new poppulaton is : ",sum(fitness_list))
    if val > sum(fitness_list):
        print("".center(90,"*"))
        print("Fitness dropped, going for roulettes selection method")
        print("".center(90,"*"))
        roulettesFunction(new_population)
    else:
        print("".center(90,"*"))
        print("Fitness increased, continuing with tournament selection method")
        print("".center(90,"*"))
        tournamentFunction(new_population)
    return

#creating initial random population
create_randomPopulation()
print("Initial population is : ",initalPopulation)
#performing the genetic algorithm
roulettesFunction(initalPopulation)
#tournamentFunction(initalPopulation)
