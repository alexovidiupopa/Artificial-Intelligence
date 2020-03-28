# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:32:59 2020

@author: Alex
"""



class Pair: 
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __getitem__(self):
        return (self.__x,self.__y)
    
    def __eq__(self, other):
        if self.__x == -1 or self.__y == -1:
            return False
        return self.__x == other.__x and self.__y == other.__y

    def __hash__(self):
        return hash((self.__x, self.__y))
    
    def __str__(self):
        string='(' + str(self.__x) + ';' + str(self.__y) + ')'
        return string
    
    def getFirst(self):
        return self.__x
    
    def getSecond(self):
        return self.__y
        
    def setFirst(self, x): 
        self.__x = x
        
    def setSecond(self, y):
        self.__y = y