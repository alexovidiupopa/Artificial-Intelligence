# -*- coding: utf-8 -*-
from State import State

class Queens:
    
    def __init__(self, filename):
        self.__currentState = State()
        self.__initialState = State()
        self.__finalState = State()
        self.__readFromFile(filename)
        
    def getInitialState(self):
        return self.__initialState
    
    def getFinalState(self):
        return self.__finalState
    
    def __eq__(self, other):
        pass
    
    def __str__(self):
        return str(self.__currentState)
        
    def __readFromFile(self,filename):
        try: 
            with open (filename,'r') as fin:
                self.__n = int(fin.readline().strip('\n'))
            return True
        except Exception as e:
            print(e)
            return False
            
    def expand(self, state):
        pass
    
    def heuristic(self, state1, state2):
        pass
        
    