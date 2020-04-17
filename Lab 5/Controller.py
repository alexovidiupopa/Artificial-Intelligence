# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:53 2020

@author: Alex
"""

from Ant import Ant 

class Controller: 
    
    def __init__(self, fileName, problem): 
        self.__problem = problem
        self.__noEpoch = 0
        self.__noAnts = 0
        self.__alpha = 0.0
        self.__beta = 0.0
        self.__rho = 0.0
        self.__q0 = 0.0
        self.__pheromoneMatrices = [[[0 for i in range(problem.getSize())] for k in range(problem.getSize())] for j in range(2*problem.getSize())]
        self.__loadParameters(fileName)
  
    def __loadParameters(self, fileName):
        with open(fileName, 'r') as file:
            line = file.readline().strip()
            self.__noEpoch = int(line.replace("number of epoch:", ""))

            line = file.readline().strip()
            self.__noAnts = int(line.replace("number of ants:", ""))

            line = file.readline().strip()
            self.__alpha = float(line.replace("alpha:", ""))

            line = file.readline().strip()
            self.__beta = float(line.replace("beta:", ""))

            line = file.readline().strip()
            self.__rho = float(line.replace("rho:", ""))

            line = file.readline().strip()
            self.__q0 = float(line.replace("q0:", ""))
            
    def __epoch(self):
        # init ants 
        population = []
        for i in range(self.__noAnts):
            ant = Ant(self.__problem)
            population.append(ant)

        # a path is complete when it has 2 n^2 elements (so it forms a nxn matrix of pairs)
        for i in range(2 * (self.__problem.getSize() ** 2)):
            for ant in population:  # for each ant, update 2n^2 times 
                ant.update(self.__pheromoneMatrices[i//self.__problem.getSize()], self.__alpha, self.__beta, self.__q0)  # trick to know which matrix i'm in
        
        # we need fitness+1 in case our fitness reaches 0 to avoid division by 0
        t = [1.0 / (population[i].fitness()+1) for i in range(len(population))]

        # pheromone vaporization for each matrix (i.e. 2n matrices)
        for k in range(2* self.__problem.getSize()):
            for i in range(self.__problem.getSize()):
                for j in range(self.__problem.getSize()):
                    self.__pheromoneMatrices[k][i][j] = (1 - self.__rho) * self.__pheromoneMatrices[k][i][j]
    
        # update matrix with the trace left by this epochs ants
        for ant in range(self.__noAnts): 
            for graph in range(2*self.__problem.getSize()): 
                path = population[ant].getPartOfPath(graph)
                for i in range(1, self.__problem.getSize()):
                    first = path[i-1]
                    second = path[i]
                    self.__pheromoneMatrices[graph][first][second] = self.__pheromoneMatrices[graph][first][second] + t[ant] 
        
        # return most fit ant (substract the 1 previously added)
        fitness = [[population[i].fitness()-1, i] for i in range(len(population))]
        fitness = min(fitness)
        return population[fitness[1]]

    def runAlgorithm(self):
        solution = None
        best_ant = None
        for i in range(self.__noEpoch):
            solution = self.__epoch()
            if best_ant == None:
                best_ant = solution
            elif solution.fitness() < best_ant.fitness():
                best_ant = solution
        return (best_ant, best_ant.fitness())