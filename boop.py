from Chromosome import Chromosome
from Constants import Constants

boop = Chromosome(30,"yaldi");
print(boop.fitness);
print(boop.chromoString);
boop.chromoString = "boopity";
print(boop.chromoString);
boop.fitness = 100;
print(boop.fitness);

print(Constants.TARGET);