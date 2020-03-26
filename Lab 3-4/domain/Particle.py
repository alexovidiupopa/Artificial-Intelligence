# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:53:03 2020

@author: Alex
"""

import random
import itertools
import copy
from domain.Pair import Pair

class Particle:
    
    def __init__(self, n, vmin, vmax):
        self.__n = n
        self.__velocity = [[random.randint(vmin,vmax), random.randint(vmin,vmax)] for i in range(n)]
        self.__cells = [[Pair(-1,-1) for i in range (n)] for j in range(n)] #cells = position
        self.generateIndividual()
        self.__bestPosition = copy.deepcopy(self)
        self.__bestFitness = self.fitness()
        
    
    def __generateLine(self):
        line=[Pair(-1,-1)  for i in range(self.__n)]
        self.__permutations = list(itertools.permutations(list(range(1,self.__n+1))))    
        p1 = random.choice(self.__permutations)
        p2 = random.choice(self.__permutations)
        for i in range(self.__n):
            [a,b] = [p1[i],p2[i]]
            line[i]=Pair(a,b)
        return line
    
    def generateIndividual(self):
        for i in range (self.__n):
            self.__cells[i] = self.__generateLine()
            
    def __getColumn(self, i):
        col = set()
        for row in self.__cells:
            col.add(row[i])
        return col
    
    def __str__(self):
        string = ""
        for i in range(self.__n):
            for p in self.__cells[i]:
                string+=str(p) + " "
            string+="\n"
        return string
                
    
    def getLine(self, i):
        return self.__cells[i][:]
            
    def setLine(self, i, values):
        self.__cells[i] = values
    
    def getLineFromS(self, i):
        values=[]
        for j in range(self.__n):
            values.append(self.__cells[i][j].getFirst())
        return values 
    
    def getLineFromT(self, i):
        values=[]
        for j in range(self.__n):
            values.append(self.__cells[i][j].getSecond())
        return values 
    
    def setLineFromS(self, i, newLine):
        for j in range(self.__n):
            self.__cells[i][j].setFirst(newLine[j])
        if self.fitness()<self.getBestFitness():
            self.__bestFitness = self.fitness()
            self.__bestPosition = copy.deepcopy(self)
            
    def setLineFromT(self, i, newLine):
        for j in range(self.__n):
            self.__cells[i][j].setSecond(newLine[j])
        if self.fitness()<self.getBestFitness():
            self.__bestFitness = self.fitness()
            self.__bestPosition = copy.deepcopy(self)    
            
    def __wrongColumns(self):
        count=0
        values = set(i+1 for i in range(self.__n))
        for j in range(self.__n):
            valuesFromS = set()
            valuesFromT = set()
            for i in range(self.__n):
                valuesFromS.add(self.__cells[i][j].getFirst())
                valuesFromT.add(self.__cells[i][j].getSecond())
            if valuesFromS!=values or valuesFromT!=values:
                count+=1
                
        return count 
    
    def __duplicateCells(self):
        matrix = set()
        for i in range (self.__n):
            for j in range(self.__n):
                matrix.add(self.__cells[i][j])
        return self.__n*self.__n - len(matrix)
    
    def fitness(self):
        return self.__wrongColumns() + self.__duplicateCells()
    
    def getNeighbours(self, howmany):
        neighbours = []
        for i in range (self.__n):  # take each line and perform permutation
            perms = list(itertools.permutations(self.__cells[i]))
            for perm in perms:
                cpy = copy.deepcopy(self)
                cpy.setLine(i, perm)
                neighbours.append(cpy)
        sorted(neighbours, key=lambda x: x.fitness())
        return neighbours[:howmany]
           
    def setCells(self, cells):
        self.__cells = cells

    def getVelocity(self):
        return self.__velocity
        
        
    def getBestFitness(self):
        return self.__bestFitness
    
    def getBestPosition(self):
        return self.__bestPosition 
    
        