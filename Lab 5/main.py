# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:28:12 2020

@author: Alex
"""

from Problem import Problem
from Controller import Controller 

def run(): 
    
    problem = Problem('aco.in')
    controller = Controller('aco-params.in', problem)
    
    pheromoneMatrices = [[1 for i in range(problem.getSize())] for j in range(2*problem.getSize())]
    
    print("computing solution")
    solution = None
    best_ant = None
    for i in range(controller.getNoEpoch()):
        solution = controller.epoch(pheromoneMatrices)
        if best_ant == None:
            best_ant = solution
        if solution.fitness() < best_ant.fitness():
            best_ant = solution
    print("{} fitness {}".format(best_ant, best_ant.fitness()))
    
run()