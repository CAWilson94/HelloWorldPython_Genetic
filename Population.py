"""
Created on 14 November 2016
@author: Charlotte Alexandra Wilson

Last revision: 14 Nov 2016 

Creates the population needed for chromosomes
"""
from Constants import Constants

class Population():
	
	def getRandPop(self):
		popSize = Constants.POP_SIZE;
		if((popSize % 2 ) != 0):
			popSize +=1;
			print(popSize);
		
		

"""
Just testing things here
"""
boop = Population();
boop.getRandPop();