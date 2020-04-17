# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 13:40:06 2020

@author: Alex
"""
from controller import Controller 
from statistics import mean, stdev

def main():
    ctrl = Controller('data\\balance-scale.data')
    accuracies = []
    print("Computing 1000 runs of training+testing.\nWill show all the runs with accuracy >= 83%\n")
    
    for i in range(1000): 
        acc = ctrl.run()
        if acc>=83:
            print("Run {} - accuracy {}%".format(i,acc))
        accuracies.append(acc)
        
    print("\nMean value is:{}%".format(mean(accuracies)))
    print("Standard deviation is:{}%".format(stdev(accuracies)))
    
main()