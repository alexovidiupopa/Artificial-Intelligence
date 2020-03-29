# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:53 2020

@author: Alex
"""

from Ant import Ant 

class Controller: 
    
    def __init__(self, fileName, problem): 
        self.params_file = fileName
        self.__problem = problem
        self.__noEpoch = 0
        self.__noAnts = 0
        self.__alpha = 0.0
        self.__beta = 0.0
        self.__rho = 0.0
        self.__q0 = 0.0
        self.loadParameters()
        
    def getNoEpoch(self):
        return self.__noEpoch

    def getNoAnts(self):
        return self.__noAnts

    def getAlpha(self):
        return self.__alpha

    def getBeta(self):
        return self.__beta

    def getRho(self):
        return self.__rho

    def getQ0(self):
        return self.__q0
    
    def run(self): 
        pass 
    
    def loadParameters(self):
        with open(self.params_file, 'r') as file:
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
            
    def epoch(self, pheromoneMatrices):
        population = []
        for i in range(self.__noAnts):
            ant = Ant(self.__problem)
            population.append(ant)

        for i in range(2 * self.__problem.getSize() ** 2):
            for j in range(len(population)): #foreach ant
                population[j].update(pheromoneMatrices[j], self.__alpha, self.__beta, self.__q0) 

        t = [1.0 / population[i].fitness() for i in range(len(population))]

        for k in range(len(population)):
            for i in range(self.__problem.getNumberOfComputers()):
                for j in range(self.__problem.getNumberOfTasks()):
                    pheromoneMatrices[k][i][j] = (1 - self.__rho) * pheromoneMatrices[k][i][j]

        for i in range(len(population)):
            for j in range(len(population[i].getPath()) - 1):
                x = population[i].getPath()[j]
                y = population[i].getPath()[j + 1]

                pheromoneMatrices[i][x][y] = pheromoneMatrices[i][x][y] + t[i]
        fitness = [[population[i].fitness(), i] for i in range(len(population))]
        fitness = min(fitness)
        return population[fitness[1]]