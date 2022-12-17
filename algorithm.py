from numpy.random import randint
from numpy.random import rand

class Genetic:
	def __init__(self):
		self.n = 10
		self.a = 1023
		self.c = 0
		self.l = 10
		self.yz = 91
		self.t = 1000
		self.p_cross = (0.50 + self.yz /100)
		self.p_mut = (0.003 + self.yz/10000)
		bounds = [[-5.0, 5.0], [-5.0, 5.0]]
		best, score = self.genetic_algorithm(self.fitness_function, bounds)
		print('Done!')
		decoded = self.decode(bounds, self.l, best)
		print('f(%s) = %f' % (decoded, score))
  
	def election(self, population, scores, k=3):
		index = randint(len(population))
		for i in randint(0, len(population), k-1):
			if scores[i] < scores[index]:
				index = i
		return population[index]

	def decode(self, bounds, n_bits, genome):
		decoded = list()
		largest = 2**n_bits
		for i in range(len(bounds)):
			start, end = i * n_bits, (i * n_bits)+n_bits
			substring = genome[start:end]
			chars = ''.join([str(s) for s in substring])
			integer = int(chars, 2)
			value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
			decoded.append(value)
		return decoded

	def fitness_function(self, x):
			return x[0]**2.0 + x[1]**2.0

	def recombination(self, parent_1, parent_2, children):
		p_cross = self.p_cross
		temp = rand()
		if temp < p_cross:
			pt = randint(1, len(parent_1)- 2)
			children[0] = parent_1[:pt] + parent_2[pt:]
			children[1] = parent_2[:pt] + parent_1[pt:]

	def crossover(self, parent_1, parent_2):
		p_cross = self.p_cross
		children = [parent_1.copy(), parent_2.copy()]
		self.recombination(parent_1, parent_2, children)
		return [children[0], children[1]]

	def exchange_genome(self, genome, i):
		genome[i] = 1 - genome[i]
		
	def mutation(self, genome):
		p_mut = self.p_mut
		for i in range(len(genome)):
			temp = rand()
			if temp < p_mut:
				self.exchange_genome(genome, i)
				
	def genetic_algorithm(self, fitness_function, bounds):
		l = self.l
		t = self.t
		n = self.n
		p_cross = self.p_cross
		p_mut = self.p_mut
		pop = [randint(0, 2, l*len(bounds)).tolist() for _ in range(n)]
		best, best_eval = 0, fitness_function(self.decode(bounds, l, pop[0]))
		for gen in range(t):
			decoded = [self.decode(bounds, l, p) for p in pop]
			scores = [fitness_function(d) for d in decoded]
			for i in range(n):
				if scores[i] < best_eval:
					best, best_eval = pop[i], scores[i]
					print("Generation: %d, new best genome: %s = %f" % (gen,  decoded[i], scores[i]))
			selected = [self.election(pop, scores) for _ in range(n)]
			children = list()
			for i in range(0, n, 2):
				p1, p2 = selected[i], selected[i+1]
				for c in self.crossover(p1, p2):
					self.mutation(c)
					children.append(c)
			pop = children
		return [best, best_eval]
