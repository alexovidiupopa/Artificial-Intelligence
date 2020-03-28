# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:57:19 2020

@author: Alex
"""

from domain.EvolutionaryAlgorithm import EA
from domain.HillClimbing import HC
from domain.ParticleSwarmOptimisation import PSO
from statistics import mean, stdev
from qtpy.QtCore import QThread
from PyQt5.QtCore import pyqtSignal

"""
use qthread to send values at each 100th iteration back to the main thread
"""
class EAStats(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self, fileName):
        QThread.__init__(self)
        self.__fileName = fileName
    
    def __readEAStats(self, fileName):
        with open(fileName,'r') as fin:
            n=int(fin.readline())
            pop_size=int(fin.readline())
            runs=int(fin.readline())
            generations=int(fin.readline())
            prob_mut=float(fin.readline())
            prob_cross=float(fin.readline())
            return n,pop_size,runs,generations,prob_mut,prob_cross
            
    def run(self):
        n, pop_size, runs, generations, prob_mut, prob_cross = self.__readEAStats(self.__fileName)
        bestSols = []
        algo = EA()
        for i in range (runs):
            result = algo.run(generations, n, pop_size, prob_cross, prob_mut)
            bestSols.append(result[1])
            if i%100==0:
                self.signal.emit([min(bestSols), i])
        stdFit = stdev(bestSols)
        meanFit = mean(bestSols)
        self.signal.emit([stdFit, meanFit, bestSols])
    
class HCStats(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self, fileName):
        QThread.__init__(self)
        self.__fileName = fileName
        
    def __readHCStats(self, fileName):
        with open(fileName,'r') as fin:
            n=int(fin.readline())
            runs=int(fin.readline())
            return n,runs
                    
    def run(self):
        n, runs = self.__readHCStats(self.__fileName)
        bestSols = []
        algo=HC()
        for i in range (runs):
            result = algo.run(n)
            bestSols.append(result[1])
            if i%100==0:
                self.signal.emit([min(bestSols), i])
        stdFit = stdev(bestSols)
        meanFit = mean(bestSols)
        self.signal.emit([stdFit, meanFit, bestSols])
    
class PSOStats(QThread):
    signal = pyqtSignal('PyQt_PyObject')
     
    def __init__(self, fileName):
        QThread.__init__(self)
        self.__fileName = fileName
    
    def __readPSOStats(self, fileName):
        with open(fileName, 'r') as fin:
            n=int(fin.readline())
            particle_size=int(fin.readline())
            w = float(fin.readline())
            c1 = float(fin.readline())
            c2 = float(fin.readline())
            neigh_size = int(fin.readline())
            vmin = int(fin.readline())
            vmax = int(fin.readline())
            iterations = int(fin.readline())
            runs = int(fin.readline())
            return n, particle_size, w, c1, c2, neigh_size, vmin, vmax, iterations, runs
        
    def run(self):
        n, particleSize, w, c1, c2, neighbourhoodSize,vmin, vmax, iterations, runs = self.__readPSOStats(self.__fileName)
        bestSols=[]
        algo=PSO()
        for i in range (runs):
            result = algo.run(n, particleSize, w, c1, c2, vmin, vmax, neighbourhoodSize, iterations)
            bestSols.append(result[1])
            if i%100==0:
                self.signal.emit([min(bestSols), i])
        stdFit = stdev(bestSols)
        meanFit = mean(bestSols)
        self.signal.emit([stdFit, meanFit, bestSols])
    