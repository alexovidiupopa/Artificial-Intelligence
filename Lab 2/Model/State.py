# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:23:12 2020

@author: Alex
"""


class State:
    
    def __init__(self):
        self.__values=[]
        self.__n=None
        pass
    
    def getValues(self):
        return self.__values[:]
    
    def setValues(self, values):
        self.__values = values
        
    def __str__(self):
        string=""
        for i in range(self.__n):
            for j in range(self.__n):
                string+=str(self.__values[i][j])+" "
            string+="\n"
        return string
            