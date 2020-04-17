# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:58 2020

@author: Alex
"""

from random import random, choice, shuffle
from copy import deepcopy
from Pair import Pair

class Ant: 
    
    def __init__(self, problem):
        self.__problem = problem 
        self.__n = problem.getSize()
        self.__path = []
        self.__visited = [] # visited will keep track of the nodes visited in the current graph
        self.__pool = [i for i in range(self.__n)] # pool of numbers to choose from (i.e. graph permutation)
        shuffle(self.__pool)
    
    def getPartOfPath(self, i):
        return self.__path[i]
    
    def __isNodeVisited(self, node):
        return node in self.__visited
    
    def __nextMoves(self): 
        moves=[]
        for number in self.__pool: 
            if self.__isNodeVisited(number) is False: 
                moves.append(number)
        return moves
    
    def __changeGraph(self):
        self.__path.append(deepcopy(self.__visited))
        self.__visited = []
        shuffle(self.__pool)
        
    def update(self, pheromoneMatrix, alpha, beta, q0):  
        # add another node aka number to the path
        if self.__visited == []: # here we basically start over in a new graph   
            self.__visited.append(choice(self.__pool))
        else: 
            if len(self.__visited)!=self.__n-1:  # current graph has more than 1 node left to explore     
                previous = self.__visited[-1]
                moves = self.__nextMoves()
                m = len(moves)
                
                #the beta power is discarded because it will always be 1^beta = 1 in my case 
                product = [1 for i in range(m)]
                product = [(pheromoneMatrix[previous][moves[i]] ** alpha) for i in range(m)]
                
                if random()<q0: 
                    #add next node
                    product = [ [i, product[i]] for i in range(m) ]
                    best = max(product, key=lambda x: x[1])             
                    self.__visited.append(moves[best[0]])     
                
                else: 
                    s = sum (product)
                    if s==0: 
                        self.__visited.append(choice(moves)) #add random with respect to uniform distribution
                    else:
                        product = [product[i]/s for i in range(m)]
                        product = [sum(product[0:i+1]) for i in range(m)]
                        r=random()
                        i=0
                        while i<m and r > product[i]:
                            i+=1
                        self.__visited.append(moves[i])
            
            else: #current graph has 1 node left to explore, find it and change the graph (i.e. the pool)
                for number in self.__pool: 
                    if self.__isNodeVisited(number) is False:    
                        self.__visited.append(number)
                        self.__changeGraph()
                        break
                    
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
    
    """
    util function to compress final path into a matrix of pairs
    """
    def __compressPath(self): 
        path = []
        for exploredGraph in self.__path: 
            for node in exploredGraph: 
                path.append(node+1) 
        compressed = []
        line = []
        for i in range(0,len(path)-1,2):
            line.append(Pair(path[i],path[i+1]))
            if len(line)%self.__problem.getSize()==0:
                compressed.append(line)
                line=[]
        return compressed
    
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
    
    