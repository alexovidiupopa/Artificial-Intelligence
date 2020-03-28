# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:28:04 2020

@author: Alex
"""
import itertools 
from random import choice

class Problem: 
    
    def __init__(self, fileName): 
        self.__fileName = fileName
        self.__n = self.__loadProblem()
        self.__graphs = self.buildGraphs()
        
    def __loadProblem(self):
        with open(self.__fileName, 'r') as f: 
            n = int(f.readline())
        return n
    
    def buildGraphs(self): 
        graphs = []
        perms = list(itertools.permutations(range(1,self.__n+1)))
        for i in range(2*self.__n): 
            graphs.append(choice(perms))
        return graphs
    
    def getSize(self):
        return self.__n
    
    def getGraphs(self):
        return self.__graphs
    
    def getCertainGraph(self, i): 
        return self.__graphs[i]