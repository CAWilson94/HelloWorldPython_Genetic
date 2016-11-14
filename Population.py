"""
Created on 14 November 2016
@author: Charlotte Alexandra Wilson

Last revision: 14 Nov 2016 

Creates the population needed for chromosomes
"""
from Constants import Constants
from Chromosome import Chromosome

class Population():
	
	def getRandPop(self):
		popSize = Constants.POP_SIZE;
		if((popSize % 2 ) != 0):
			popSize +=1;
			print(popSize);
		population = [];
		for index in range((popSize)):
			chromosomeNew = Chromosome();
			population.append(); # Want random number generated in chromosome class instead

		return population;

"""
(1) : want to have more than one constructor for the chromosome
Just testing things here
"""
boop = Population();
boop.getRandPop();