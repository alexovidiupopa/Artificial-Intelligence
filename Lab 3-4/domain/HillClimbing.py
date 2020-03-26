# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:43:30 2020

@author: Alex
"""


from domain.Individual import Individual
import copy 
from qtpy.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class HC:
    
    def __init__(self):
        pass
    
    def run(self,n):
        currentNode = Individual(n)
        
        while currentNode.fitness() > 0:
            neighbours = currentNode.getNeighbours()
            neighbours.sort(key=lambda b: b.fitness())
            bestNeighbour = neighbours[0]
            
            if bestNeighbour.fitness() < currentNode.fitness():
                currentNode = copy.deepcopy(bestNeighbour)
            else:
                return (currentNode, currentNode.fitness())
        
        return (currentNode, currentNode.fitness())
    
class HCThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self,n):
        QThread.__init__(self)
        self.__n = n
    
    def run(self):
        currentNode = Individual(self.__n)
        
        while currentNode.fitness() > 0:
            neighbours = currentNode.getNeighbours()
            neighbours.sort(key=lambda b: b.fitness())
            bestNeighbour = neighbours[0]
            
            if bestNeighbour.fitness() < currentNode.fitness():
                currentNode = copy.deepcopy(bestNeighbour)
            else:
                self.signal.emit([currentNode, currentNode.fitness(),"done"])
                return
        
        self.signal.emit([currentNode, currentNode.fitness(),"done"])
        