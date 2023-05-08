from random import choices
from random import randrange
from random import uniform
import matplotlib.pyplot as plt

genes = ["I","N","D","A"]
targetString =["I","N","D","I","A"]
initalPopulation=[]
n=4

#creating initial random population
def create_randomPopulation():
    global genes, initalPopulation
    #20 individual in the random population
    for i in range(20):
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
    print("Matching individual's character positions with 'INDIA' character position to find the fitness of the indvidual.") 
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


def roulettesFunction(population):
    global n
    print("".center(90,"*"))

    fitness_list=[]
    probability_list=[]
    new_population=[]
    #find the fitness and probability of the population
    fitness_list,probability_list = determineFitness(population)
    plt.pie(probability_list,labels = population)
    plt.show()
    #using roulettes wheel to select fit population as parents
    #here 4 fittest parents are choosen ot of the 20 individuals 
    parents = choices(population,weights=probability_list,k=n)

    print("".center(90,"*"))
    #print parents found
    print("Fittest Parents selected with roulettes wheel from the population are : ",parents)
    print("".center(90,"*"))
    #find the fitness and probability of the parents
    fitness_list,probability_list = determineFitness(parents)
    
    plt.pie(probability_list,labels = parents)
    plt.show()
    #return parents found
    return parents


#creating initial random population
create_randomPopulation()
print("Initial population is : ",initalPopulation)
#performing the genetic algorithm
parents = roulettesFunction(initalPopulation)
