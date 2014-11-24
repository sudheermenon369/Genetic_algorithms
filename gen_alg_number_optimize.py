""" This progam takes a look into a simple gen_alg model to optimize the set of
5 numbers which gives a total sum of 200"""

from random import randint,random
from operator import add


'Building an individual'

def individual(length,min,max):
	'Create a member of the population'
	return [ randint(min,max) for x in xrange(length)]



'Creating a whole population'

def population(count,length,min,max):
	return [individual(length,min,max) for x in xrange(count)]



' Creating a fitness function (distance of the sum(members) of the individual to the sum'

def fitness (individual,target):

	'Lower fitness the better'
	'Best individual has a fitness value of 0.0'

	sum = reduce(add,individual,0)

	return abs(target - sum)



'Calculating the average population fitness'

def grade(population,target):

	summed = reduce(add, (fitness(x,target) for x in population),0)
	print type(x)
	return summed / (len(population) * 1.0)



'Lets go with the simple_crossovers'

def simple_crossover(parents,population):

	parents_length = len(parents)
	print 'parents length = ', parents_length
	desired_length = len(population) - parents_length
	print 'desired length = ', desired_length
	children = []
	while len(children) < desired_length:
		male = randint(0,parents_length - 1)
		female = randint(0,parents_length - 1)
		if male != female:
			male = parents[male]
			female = parents[female]
			half = len(male) / 2
			child = male[:half] + female[half:]
			children.append(child)

	parents.extend(children)
	return parents



' Lets start with the evolution process'

def evolve(population, target, retain = 0.2, random_select = 0.05 , mutate = 0.01):
	
	graded = [ (fitness(x,target), x) for x in population]
	graded = [ x[1] for x in sorted(graded)]
	retain_length = int(len(graded)*retain)
	parents = graded[:retain_length]

	'Randomly selecting other individuals - promote diversity in population'	

	for individual in graded[retain_length: ] :
		if random_select > random():
			parents.append(individual)

	'Lets make some mutants'

	for individual in parents:
		if mutate > random():
			pos_to_mutate = randint(0,len(individual)-1)
			individual[pos_to_mutate] = randint(min(individual), max(individual))

	return(simple_crossover(parents,population))



'Lets make it run'

target = 371
population_count = 100
individual_length = 5
individual_min = 0
individual_max = 100
p = population(population_count,individual_length,individual_min,individual_max)
fitness_history = [grade(p,target) ,]
for i in xrange(100):
	p = evolve(p,target)
	fitness_history.append(grade(p,target))

print fitness_history