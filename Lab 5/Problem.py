# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:28:04 2020

@author: Alex
"""

class Problem: 
    
    def __init__(self, fileName): 
        self.__fileName = fileName
        self.__n = self.__loadProblem()
        
    def __loadProblem(self):
        with open(self.__fileName, 'r') as file: 
            line = file.readline().strip()
            n = int(line.replace("n:", ""))
        return n
    
    def getSize(self):
        return self.__n
