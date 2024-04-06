
import random

class GeneticSolver(object):

    def __init__(self, genes=None, target=None, chromosome=None):
        self.genes = genes
        self.target =target
        if chromosome == None:
            self.chromosome = self.create_gnome()
        else:   
            self.chromosome = chromosome
        self.fitness = self.fitness()

    def mutated_genes(self):
        return random.choice(self.genes)

    def create_gnome(self):

    # Create chromosome

        gnome_len = len(self.target)
        return [self.mutated_genes() for _ in range(gnome_len)]

    def mate(self, parent2):

        # chromosome for offspring

        child = []
        for (p1, p2) in zip(self.chromosome, parent2.chromosome):

        # random probability
            prob = random.random()

            if prob < 0.48:
                child.append(p1)
            elif prob < 0.96:
                child.append(p2)
            else:
                child.append(self.mutated_genes())

        return GeneticSolver(parent2.genes,parent2.target, child)

    def fitness(self):

        fitness = 0
        for (p1, p2) in zip(self.chromosome, self.target):
            if p1 != p2:
                fitness += 1
        return fitness      

    def genetic_algorithm(self, population_list, population_size):
        generation = 1
        found = False
        population = population_list
        while not found:
            # sort the population in increasing order of fitness score
            population = sorted(population, key=lambda x: x.fitness)
            if population[0].fitness <= 0:
                found = True
                break
            # Generate new offsprings for new generation
            new_generation = []
            # Perform Elitism
            s = int(10 * population_size / 100)
            new_generation.extend(population[:s])
            s = int(90 * population_size / 100)
            for _ in range(s):
                parent1 = random.choice(population[:50])
                parent2 = random.choice(population[:50])
                child = parent1.mate(parent2)
                new_generation.append(child)
            population = new_generation
            print ('Generation: {}\tString: {}\tFitness: {}'.format(generation,''.join(population[0].chromosome),population[0].fitness))
            generation += 1
        print ('Generation: {}\tString: {}\tFitness: {}'.format(generation,''.join(population[0].chromosome),population[0].fitness))