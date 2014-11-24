

from random import randint, random
from deap import base, creator, tools , algorithms
import numpy
from operator import add

target = 371

'Creating an individual'

creator.create("fitnessMin",base.Fitness,weights = (0.0,))
creator.create("individual",list,fitness = creator.fitnessMin)

toolbox = base.Toolbox()
toolbox.register("Elements",randint,0,100)
toolbox.register("Individual",tools.initRepeat,creator.individual,toolbox.Elements,n = 5)

'Creating a Population of individuals'

toolbox.register("Population",tools.initRepeat,list,toolbox.Individual,n = 3)


def fitness (individual):

	'Lower fitness the better'
	'Best individual has a fitness value of 0.0'

	sum = reduce(add,individual,0)

	return abs(target - sum)


'Calculating the average population fitness'

def grade(individual):
	
	summed = reduce(add,individual,0)
	return summed / (len(individual) * 1.0)

toolbox.register("evaluate",grade)
toolbox.register("Crossover",tools.cxOnePoint)
toolbox.register("Mutate",tools.mutUniformInt,indpb = 0.01)
toolbox.register("Selection",tools.selBest)


def evolution():
	pop = toolbox.Population(n = 100)
	hof = tools.HallOfFame(1)
	stats = tools.Statistics(lambda ind: ind.fitness.values)
	stats.register("avg", numpy.mean)
	stats.register("min",numpy.min)
	stats.register("max", numpy.max)

	pop , logbook = algorithms.eaSimple(pop,toolbox, cxpb = 0.2, mutpb = 0.01, ngen = 10, stats = stats, halloffame = hof, verbose = True)

	return pop,logbook,hof

pop, log , hof = evolution()

print("Best individual is: %s\nwith fitness: %s" % (hof[0], hof[0].fitness))