# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:04:26 2020

@author: Alex
"""

from random import random, randint
from domain.Individual import Individual
from domain.Particle import Particle 
from math import exp
import numpy as np

class Population: 
    def __init__(self, n, pop_size, prob_gene, prob_mut):
        self.__pop_size = pop_size
        self.__prob_gene = prob_gene
        self.__prob_mut = prob_mut
        self.__n = n 
        self.__pop = self.generatePop()
        
    def generatePop(self):
        initial_pop = []
        for i in range (self.__pop_size):
            individual = Individual(self.__n)
            initial_pop.append(individual)
        return initial_pop[:]
    
    def getPop(self):
        return self.__pop
    
    def naturalSelection(self):
        return sorted(self.__pop, key=lambda x: x.fitness())[:self.__pop_size]

    def iteration(self):
        """
        take two random parents and perform crossover to get two children
        perform natural selection (i.e. sort and remove the two least fit from the population)
        """
        i1 = randint(0, self.__pop_size-1)
        i2 = randint(0, self.__pop_size-1)
        if i1!=i2:
            child1, child2 = self.__pop[i1].crossover(self.__pop[i2],self.__prob_gene)
            child1.mutate(self.__prob_mut)
            child2.mutate(self.__prob_mut)
            self.__pop.append(child1)
            self.__pop.append(child2)
        self.__pop = self.naturalSelection()
   
     
class PSOPopulation:
    def __init__(self, n, particleSize, vmin, vmax):
        self.__n = n
        self.__particleSize = particleSize
        self.__vmin = vmin
        self.__vmax = vmax 
        self.__pop = self.generatePop()
        
    def generatePop(self):
        initial_pop = []
        for i in range (self.__n):
            particle = Particle(self.__particleSize, self.__vmin, self.__vmax)
            initial_pop.append(particle)
        return initial_pop[:]
    
    def getBest(self):
        # sorted(self.__pop, key=lambda x: x.fitness())
        self.__pop.sort(key=lambda x: x.fitness())
        return self.__pop[0]
    
    def selectNeighbours(self, size):
        neighbours = []
        for p in self.__pop:
            neighbours+=p.getNeighbours(size)
        return neighbours 
    
    def __sigmoidFunction(self, v): #compute the value of the sigmoid function for a given velocity (i.e. s(v ij) from the lecture pdf)
        return exp(-np.logaddexp(0, -v)) 
    
    def __manhattanDistance(self, line1, line2):
        dist = 0
        for i in range(len(line1)):
            dist+=line1[i]-line2[i]
        return dist
    
    def iteration(self, neighbours, c1, c2, w):
        
        """
        get best neighbours so far 
        """
        bestneigh=[]
        for i in range(len(self.__pop)):
            bestneigh.append(neighbours[0])
            for j in range (1, len(neighbours)):
                if bestneigh[i].fitness()<neighbours[j].fitness():
                    bestneigh[i]=neighbours[j]
        
        """
        compute new velocities for each x and y in (x,y) (i.e. values from S and T respectively)
        """
        for i in range(len(self.__pop)):
            for j in range(len(self.__pop[0].getVelocity())):
                newVelocityS = w * self.__pop[i].getVelocity()[j][0] \
                                + c1 * random() * (self.__manhattanDistance(bestneigh[i].getLineFromS(j), self.__pop[i].getLineFromS(j))) \
                                + c2 * random()* (self.__manhattanDistance(self.__pop[i].getBestPosition().getLineFromS(j), self.__pop[i].getLineFromS(j)))
                newVelocityT = w * self.__pop[i].getVelocity()[j][1] \
                               + c1 * random() * (self.__manhattanDistance(bestneigh[i].getLineFromT(j), self.__pop[i].getLineFromT(j))) \
                               + c2 * random()* (self.__manhattanDistance(self.__pop[i].getBestPosition().getLineFromT(j), self.__pop[i].getLineFromT(j)))
                self.__pop[i].getVelocity()[j][0] = newVelocityS
                self.__pop[i].getVelocity()[j][1] = newVelocityT
        
        """
        change the values from S/T if the value given by the sigmoid function for the velocity > random nr (t) in [0,1]
        """
        for i in range(len(self.__pop)):
            for j in range(len(self.__pop[0].getVelocity())):
                if random() < self.__sigmoidFunction(self.__pop[i].getVelocity()[j][0]):
                    self.__pop[i].setLineFromS(j, bestneigh[i].getLineFromS(j))
                if random() < self.__sigmoidFunction(self.__pop[i].getVelocity()[j][1]):
                    self.__pop[i].setLineFromT(j, bestneigh[i].getLineFromT(j))
    
    