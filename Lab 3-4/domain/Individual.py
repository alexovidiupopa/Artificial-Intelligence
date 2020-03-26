# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:04:16 2020

@author: Alex
"""

import random
import itertools
import copy
from domain.Pair import Pair

class Individual: 
    
    def __init__(self, size):
        self.__cells = [[Pair(-1,-1) for i in range (size)] for j in range(size)]
        self.__size = size
        self.generateIndividual()
        
    def __generateLine(self):
        line=[Pair(-1,-1)  for i in range(self.__size)]
        self.__permutations = list(itertools.permutations(list(range(1,self.__size+1))))    
        p1 = random.choice(self.__permutations)
        p2 = random.choice(self.__permutations)
        for i in range(self.__size):
            [a,b] = [p1[i],p2[i]]
            line[i]=Pair(a,b)
        return line
    
    def generateIndividual(self):
        for i in range (self.__size):
            self.__cells[i] = self.__generateLine()
            
    def __getColumn(self, i):
        col = set()
        for row in self.__cells:
            col.add(row[i])
        return col
    
    def __str__(self):
        string = ""
        for i in range(self.__size):
            for p in self.__cells[i]:
                string+=str(p) + " "
            string+="\n"
        return string
                
    
    def getLine(self, i):
        return self.__cells[i][:]
            
    def setLine(self, i, values):
        self.__cells[i] = values
    
    def crossover(self, other, prob_cros):
        n=self.__size
        child1 = Individual(n)
        child2 = Individual(n)
        for i in range(n):
            if prob_cros>random.random(): #set the lines into the two children combining the two parents
                child1.setLine(i, copy.deepcopy(self.__cells[i]))
                child2.setLine(i, copy.deepcopy(other.getLine(i)))
            else:
                child1.setLine(i, copy.deepcopy(other.getLine(i)))
                child2.setLine(i, copy.deepcopy(self.__cells[i]))
        return child1, child2
     
    def __wrongColumns(self):
        count=0
        values = set(i+1 for i in range(self.__size))
        for j in range(self.__size):
            valuesFromS = set()
            valuesFromT = set()
            for i in range(self.__size):
                valuesFromS.add(self.__cells[i][j].getFirst())
                valuesFromT.add(self.__cells[i][j].getSecond())
            if valuesFromS!=values or valuesFromT!=values:
                count+=1          
        return count 
    
    def __duplicateCells(self):
        matrix = set()
        for i in range (self.__size):
            for j in range(self.__size):
                matrix.add(self.__cells[i][j])
        return self.__size*self.__size - len(matrix)
    
    def fitness(self):
        return self.__wrongColumns() + self.__duplicateCells()
            
    def mutate(self, prob_mut):
        for i in range(self.__size):
            if prob_mut>random.random(): #shuffle with regards to the probability    
                random.shuffle(self.__cells[i])
                  
    def getNeighbours(self):
        neighbours = []
        for i in range (self.__size):  # take each line and perform permutation
            perms = list(itertools.permutations(self.__cells[i]))
            for perm in perms:
                cpy = copy.deepcopy(self)
                cpy.setLine(i, perm)
                neighbours.append(cpy)
        return neighbours 
            
    