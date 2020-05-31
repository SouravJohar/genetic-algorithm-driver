from random import *
import math
from numpy import interp


class Evolution:
    def __init__(species, mutation_rate=0.01, pop_size=100, elitism=0.1):
        self.mutation_rate = mutation_rate
        self.pop_size = pop_size
        self.elitism = elitism
        self.species = species

    def create():
        init_pop = [self.species.create_random_organism()
                    for i in range(self.pop_size)]
        self.species.population.extend(init_pop)

    def evolve(num_generations=1, fitness_thresh=None, evolve_until_thresh_reached=False):
        gen_counter = 1

        if evolve_until_thresh_reached:
            num_generations = math.inf

        while gen_counter <= num_generations:
            # sort the population in descending order of fitness
            self.species.population.sort(
                key=lambda x: self.species.fitness_function(x), reverse=True)
            print("GENERATION: {0} - MAX_FITNESS: {1}".format(
                gen_counter, self.get_fittest_organisms()[1]))

            # check if goal has been reached
            if fitness_thresh:
                organism, fitness = self.get_fittest_organisms(n=1)
                if fitness >= fitness_thresh:
                    return organism, fitness

            # if not, start evolution
            self.species.population = []
            if elitism:
                # elites get to be a part of the next generation as is
                # TODO: mutate the elites?
                num_elites = int(elitism * self.pop_size)
                selected_elites = list(zip(*self.get_fittest_organisms(n=num_elites)))[0]
                self.species.population = selected_elites
            for _ in range(self.pop_size - len(self.species.population)):
                self.species.population.append(self.species.create_offspring(mutation_rate=mutation_rate))

            gen_counter += 1

    def get_fittest_organisms(n=1):
        if n > self.pop_size:
            raise Exception(
                "Tried to get {0} fittest organisms in a population of {1}".format(n, self.pop_size))
        if n == 1:
            return self.species.population[0], self.species.fitness_function(self.species.population[0])

        element_fitness_pairs = []
        for element in self.species.population[0:n - 1]:
            fitness = self.species.fitness_function(element)
            element_fitness_pairs.append((element, fitness))
        return element_fitness_pairs


class Species:
    def __init__(gene_pool,
                 gene_length,
                 fitness_function,
                 custom_gene=None,
                 custom_gene_args=None,
                 custom_crossover=None,
                 custom_crossover_args=None,
                 custom_mutate=None,
                 custom_mutate_agrs=None):
        pass

    def create_random_organism():
        pass

    def create_offspring(population, mutation_rate=0.01):
        pass

    def crossover(type='split'):
        pass

    def mutate():
        pass

    def _select_potential_parents(num_parents=2):
        pass



#
# def createPool(fitness, pop):
#     matingPool = []
#     maxFitness = max(fitness)
#     for i in range(len(fitness)):
#         n = interp(fitness[i], [0, maxFitness], [0, 1])
#         n = int(math.floor(n * 100))
#         for j in range(n):
#             matingPool.append(pop[i])
#     return matingPool
#
# 
# def crossOver(matingPool):
#     partners = sample(matingPool, 2)
#     splitPoint = randint(0, N - 1)
#     child = partners[0][:splitPoint] + partners[1][splitPoint:]
#     return child
#
#
# def mutate(child):
#     for i in range(len(child)):
#         if random() < mutationRate:
#             new_row = [0 for k in range(len(child))]
#             index = randint(0, len(child) - 1)
#             new_row[index] = 1
#             child[i] = new_row
#     return child
