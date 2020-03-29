# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:58 2020

@author: Alex
"""

from random import randint, random, choice
from copy import deepcopy
from Pair import Pair

class Ant: 
    
    def __init__(self, problem):
        self.__problem = problem 
        self.__pathSize = (problem.getSize() ** 2) * 2 
        self.__path = [randint(1,problem.getSize())]
        self.__initialGraph = randint(0,2* problem.getSize()-1)
        self.__visited = [(self.__initialGraph, self.__path[0])]  
        self.__graphs = self.__problem.getGraphs()
        
    def getPath(self): 
        return self.__path 
    
    def evaluate(self):
        pass
    
    def distance(self, next):
        return 1
    
    def nextMoves(self, pos): 
        moves = []
        
        
        return moves
    
    def update(self, pheromoneMatrices, alpha, beta, q0):
        #can't update anymore
        p = [0 for i in range(self.__problem.getNumberOfTasks())]
        nextMoves = self.nextMoves()

        for i in nextMoves:
            p[i] = self.distance(i)
            
        r = [(p[i] ** beta) * (pheromoneMatrices[self.__path[-1]][i] ** alpha) for i in range(len(p))]
        rnd1 = random()
        if rnd1 < q0:
            r = [[i, p[i]] for i in range(len(p))]
            r = max(r, key=lambda a: a[1])
            self.__path.append(r[0])
        else:
            s = sum(p)
            if s == 0:
                self.__path.append(choice(nextMoves))
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0: i + 1]) for i in range(len(p))]
            rnd2 = random()
            i = 0
            while rnd2 > p[i]:
                i += 1
            self.__path.append(i)
        return True
        
    
    def __wrongColumns(self, path):
        count=0
        values = set(i+1 for i in range(self.__problem.getSize()))
        for j in range(self.__problem.getSize()):
            valuesFromS = set()
            valuesFromT = set()
            for i in range(self.__problem.getSize()):
                valuesFromS.add(path[i][j].getFirst())
                valuesFromT.add(path[i][j].getSecond())
            if valuesFromS!=values or valuesFromT!=values:
                count+=1          
        return count 
    
    def __duplicateCells(self, path):
        matrix = set()
        for i in range (self.__problem.getSize()):
            for j in range(self.__problem.getSize()):
                matrix.add(path[i][j])
        return self.__problem.getSize() ** 2 - len(matrix)
    
    def __compressPath(self): 
        path = deepcopy(self.__path)
        compressed = []
        line = []
        for i in range(0,len(path),2):
            line.append(Pair(path[i],path[i+1]))
            if len(line)%self.__problem.getSize()==0:
                compressed.append(line)
                line=[]
        return compressed
    
    def fitness(self):
        pathAsMatrix = self.__compressPath()
        return self.__wrongColumns(pathAsMatrix) + self.__duplicateCells(pathAsMatrix)
    
    def __str__(self):
        string = ""
        pathAsMatrix = self.__compressPath()
        for i in range(len(pathAsMatrix)):
            for p in pathAsMatrix[i]:
                string+=str(p) + " "
            string+="\n"
        return string