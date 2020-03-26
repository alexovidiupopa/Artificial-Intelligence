# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:45:21 2020

@author: Alex
"""

from domain.Population import PSOPopulation 
from qtpy.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class PSO:
    
    def __init__(self):
        pass
    
    def run(self, n, particleSize, w, c1, c2, vmin, vmax, neighbourhoodSize, iterations):
        p = PSOPopulation(n, particleSize, vmin, vmax)
        
        neighbours = p.selectNeighbours(neighbourhoodSize)
        
        for i in range(iterations):
            p.iteration(neighbours, c1, c2, w/(i+1))
        
        best = p.getBest()
        return (best, best.fitness()) 
        
class PSOThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self, n, particleSize, w, c1, c2, vmin, vmax, neighbourhoodSize, iterations):
        QThread.__init__(self)
        self.__n = n
        self.__particleSize = particleSize
        self.__w = w
        self.__c1 = c1
        self.__c2 = c2
        self.__vmin = vmin
        self.__vmax = vmax
        self.__neighbourhoodSize = neighbourhoodSize
        self.__iterations = iterations
    
    def run(self):
        bestSols = []
        p = PSOPopulation(self.__n, self.__particleSize, self.__vmin, self.__vmax)
        
        neighbours = p.selectNeighbours(self.__neighbourhoodSize)
        
        for i in range(self.__iterations):
            p.iteration(neighbours, self.__c1, self.__c2, self.__w/(i+1))
            bestSols.append(p.getBest().fitness())
            if i % 10 == 0: 
                self.signal.emit([min(bestSols), i])
        best = p.getBest()
        self.signal.emit([best, best.fitness(),"done"]) 