# -*- coding: utf-8 -*-

from Model.Queens import Queens

class Controller:
    
    def __init__(self, queens):
        self.__instance = queens
        
    def getInstance(self):
        return self.__instance
    
    def isSolution(self, problem):
        return problem.getInitialState()==problem.getFinalState()
    
    def orderStates(self, states):
        pass
    
    def dfs(self, instance):
        pass
    
    def greedy(self, instance):
        pass
    