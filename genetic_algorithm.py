

from random import randint
import numpy as np
import matplotlib.pyplot as plt

class GeneticAlgorithm:
    
    
    def __init__(self):
        self.n = 10                             #
        self.a = 1023                           #
        self.c = 0                              # 
        self.l = 10                             # Length of the binary string
        self.yz = 91                            # The last two digits of your studentID
        self.t = 1000                           # Number of iterations
        self.p_cross = (0.50 + self.yz /100)    # The probability of crossover
        self.p_mut = (0.003 + self.yz/10000)    # The probability of mutation
        
    def recombination(self):
        pass
    
    def crossover(self):
        pass
    
    def mutation(self):
        pass
    
    def election(self):
        # first random selection
        #selection_ix = randint(len(pop))
        #for ix in randint(0, len(pop), k-1):
        #    # check if better (e.g. perform a tournament)
        #    if scores[ix] < scores[selection_ix]:
        #        selection_ix = ix
        #return pop[selection_ix]
        election_no = randint(1023)
        
    
    def runGeneticAlgorithm(self):
        for i in range(self.t):
            self.recombination()
            self.crossover()
            self.mutation()
            self.election()

GeneticAlgorithm()