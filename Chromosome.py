"""
Created on 14 November 2016
@author: Charlotte Alexandra Wilson

Last revision: 14 Nov 2016 

Chromosome attributes set and retrieved here using the getter and setter decorator
"""

class Chromosome():
	fitness = 0;
	chromoString = "boop";

	def __init__(self, fitness, chromoString):
	 	self.fitness = fitness;
	 	self.chromoString = chromoString;

	@property
	def chromoString(self):
		return self.chromoString;
	

	@chromoString.setter
	def chromoString(self,chromoString):
		self.chromoString = chromoString;
	

	@property
	def fitness(self):
		return self.fitness;
	

	@fitness.setter
	def fitness(self,fitness):
		self.fitness = fitness;

	