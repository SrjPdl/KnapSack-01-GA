from deap import base, creator, tools, algorithms
from knapsack import KnapSack

import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

knapsack = KnapSack()

POPULATION_SIZE = 40
MAX_GENERATIONS = 30
P_MUTATION = 0.1
P_CROSSOVER = 0.9
HALL_OF_FAME_SIZE = 1
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

toolbox.register("zerosOrOnes",random.randint,0,1)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zerosOrOnes,len(knapsack))
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

def fitness(individual):
    return knapsack.getValue(individual),

toolbox.register("evaluate",fitness)
toolbox.register("select",tools.selTournament,tournsize=3)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = 1.0/len(knapsack))

def main():

    population = toolbox.populationCreator(n = POPULATION_SIZE)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("max", np.max)
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    population, logbook = algorithms.eaSimple(population, toolbox,cxpb = P_CROSSOVER, mutpb = P_MUTATION, ngen = MAX_GENERATIONS, stats = stats, halloffame = hof, verbose = True )

    best = hof[0]
    print(f"Best individual: \n{best} \nFitness: \n{best.fitness.values}\n\n")
    knapsack.printItems(best)

    maxFitnessValues, avgFitnessValues = logbook.select("max", "avg")

    sns.set_style("whitegrid")
    plt.plot(maxFitnessValues, label = "maximum")
    plt.plot(avgFitnessValues, label = "average")
    plt.title("KnapSack")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend(loc = "lower right")
    plt.show()

if __name__ == "__main__":
    main()