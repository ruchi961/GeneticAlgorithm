# GeneticAlgorithm
Contains <b>python implemention of the Genetic Algorithm</b> and the concepts involved in the Genetic Programming, such as selection operators like roulettes Function, Tournament Selection, etc.

<b>roulettePrac.py:</b> Contains the python implemntation of the roulette funcction with initial random population and further roulette selection along with the pie chart representation depicting the probability distribution.

<b>GeneticAlgorithm.py:</b> Contains the implementation of the roulette selection operator, uniform crossover an uniform mutation operator.

<b>GeneticRouletteTournament.py:</b> Contains the implementation of the roulette selection and the tournament selection operator, uniform crossover an uniform mutation operator. The logic switches between the two selection operator if one of the operator provides less fitter population. Eg. If rolette selection provides a less fitter population, ten the tournament selection operator is used for the population selection and vice-versa.
