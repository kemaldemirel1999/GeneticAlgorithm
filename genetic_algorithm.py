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
		# store
		decoded.append(value)
	return decoded

def selection(pop, scores, k=3):
	selection_ix = randint(len(pop))
	for ix in randint(0, len(pop), k-1):
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]

def crossover(p1, p2, r_cross):
	c1, c2 = p1.copy(), p2.copy()
	if rand() < r_cross:
		pt = randint(1, len(p1)-2)
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		if rand() < r_mut:
			bitstring[i] = 1 - bitstring[i]


def genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
	pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)]
	best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))
	for gen in range(n_iter):
		decoded = [decode(bounds, n_bits, p) for p in pop]
		scores = [objective(d) for d in decoded]
		for i in range(n_pop):
			if scores[i] < best_eval:
				best, best_eval = pop[i], scores[i]
				print(">%d, new best f(%s) = %f" % (gen,  decoded[i], scores[i]))
		selected = [selection(pop, scores) for _ in range(n_pop)]
		children = list()
		for i in range(0, n_pop, 2):
			p1, p2 = selected[i], selected[i+1]
			for c in crossover(p1, p2, r_cross):
				mutation(c, r_mut)
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