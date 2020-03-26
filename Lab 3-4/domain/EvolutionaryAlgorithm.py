# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:39:42 2020

@author: Alex
"""


from domain.Population import Population 
from qtpy.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

class EA:
    
    def __init__(self):
        pass
    
    def run(self,generations,n,pop_size,cross_prob,prob_mut):
        p = Population(n,pop_size, cross_prob, prob_mut)
        for i in range(generations):
            p.iteration()   
        return (p.getPop()[0], p.getPop()[0].fitness())
   
class EAThreaded(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self,generations,n,pop_size,cross_prob,prob_mut):
        QThread.__init__(self)
        self.__generations = generations
        self.__n = n
        self.__pop_size = pop_size
        self.__cross_prob = cross_prob
        self.__prob_mut = prob_mut 
        
    def run(self):
        best = []
        p = Population(self.__n,self.__pop_size, self.__cross_prob, self.__prob_mut)
        for i in range(self.__generations):
            p.iteration() 
            best.append(p.getPop()[0].fitness())
            if i % 10 == 0: 
                self.signal.emit([min(best), i])
                
        self.signal.emit([p.getPop()[0], p.getPop()[0].fitness(),"done"])
        