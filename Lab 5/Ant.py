# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:27:58 2020

@author: Alex
"""

from random import randint, random, choice

class Ant: 
    
    def __init__(self, problem):
        self.__problem = problem 
        self.__pathSize = (problem.getSize() ** 2) * 2 
        self.__path = [randint(1,problem.getSize())]
        
    def getPath(self): 
        return self.__path 
    
    def evaluate(self):
        pass
    
    def distance(self, next):
        return 1
    
    
    def update(self, traceMatrix, alpha, beta, q0):
        pass
    
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
    
    def __compressPath(self, path): 
        pass 
    
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