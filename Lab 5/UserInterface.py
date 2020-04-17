# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 18:54:53 2020

@author: Alex
"""


from Controller import Controller
from Problem import Problem 
from statistics import mean, stdev 
import matplotlib.pyplot as plt 

class Console: 

    def __aco(self):
        problem = Problem('aco.in')
        controller = Controller('aco-params.in', problem)
        solution = controller.runAlgorithm()
        print("\nBest solution is:\n{}With fitness={}".format(solution[0], solution[1]))

    def __stats(self):
        print("Input the number of iterations:")
        iterations = int(input())
        bestFitnesses = []
        for i in range(iterations): 
            problem = Problem('aco.in')
            controller = Controller('aco-stats-params.in', problem)
            solution = controller.runAlgorithm()
            bestFitnesses.append(solution[1])
            if i%75==0: 
                print("Best solution fitness until iteration {} is {}".format(i, min(bestFitnesses)))
        print("Mean value is: {}".format(mean(bestFitnesses)))
        print("Stdev is : {}".format(stdev(bestFitnesses)))
        plt.plot(bestFitnesses)
        plt.show()
        
    def run(self):         
        while True: 
            print("\n\nPress 1 for normal ACO run\nor 2 for statistical validation\nexit closes the program\n\n")
            print(">>")
            cmd = input()
            if cmd=="1":
                self.__aco()
            elif cmd=="2":
                self.__stats()
            elif cmd=="exit":
                return 
            else:
                continue
        