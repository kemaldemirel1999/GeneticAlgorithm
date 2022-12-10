from numpy.random import randint
from numpy.random import rand

def objective(x):
	return x[0]**2.0 + x[1]**2.0

def decode(bounds, n_bits, bitstring):
	decoded = list()
	largest = 2**n_bits
	for i in range(len(bounds)):
		start, end = i * n_bits, (i * n_bits)+n_bits
		substring = bitstring[start:end]
		chars = ''.join([str(s) for s in substring])
		integer = int(chars, 2)
		value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])
		decoded.append(value)
	return decoded

def election(population, scores, k=3):
	index = randint(len(population))
	for i in randint(0, len(population), k-1):
		if scores[i] < scores[index]:
			index = i
	return population[index]

def recombination(parent_1, parent_2, p_cross, children):
    temp = rand()
    if temp < p_cross:
        pt = randint(1, len(parent_1)- 2)
        children[0] = parent_1[:pt] + parent_2[pt:]
        children[1] = parent_2[:pt] + parent_1[pt:]

def crossover(parent_1, parent_2, p_cross):
	children = [parent_1.copy(), parent_2.copy()]
	recombination(parent_1, parent_2, p_cross, children)
	return [children[0], children[1]]

def exchange_genome(genome, i):
    genome[i] = 1 - genome[i]
    
def mutation(genome, p_mut):
	for i in range(len(genome)):
		temp = rand()
		if temp < p_mut:
			exchange_genome(genome, i)
			
def genetic_algorithm(objective, bounds, l, t, n, p_cross, p_mut):
	pop = [randint(0, 2, l*len(bounds)).tolist() for _ in range(n)]
	best, best_eval = 0, objective(decode(bounds, l, pop[0]))
	for gen in range(t):
		decoded = [decode(bounds, l, p) for p in pop]
		scores = [objective(d) for d in decoded]
		for i in range(n):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print("Generation: %d, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
		selected = [election(pop, scores) for _ in range(n)]
		children = list()
		for i in range(0, n, 2):
			p1, p2 = selected[i], selected[i+1]
			for c in crossover(p1, p2, p_cross):
				mutation(c, p_mut)
				children.append(c)
		pop = children
	return [best, best_eval]

n = 10                             # Number of chromosomes
a = 1023                           #
c = 0                              # 
l = 10                             # Length of the binary string
yz = 91                            # The last two digits of your studentID
t = 1000                           # Number of iterations
p_cross = (0.50 + yz /100)         # The probability of crossover
p_mut = (0.003 + yz/10000)         # The probability of mutation
bounds = [[-5.0, 5.0], [-5.0, 5.0]]

best, score = genetic_algorithm(objective, bounds, l, t, n, p_cross, p_mut)
print('Done!')
decoded = decode(bounds, l, best)
print('f(%s) = %f' % (decoded, score))