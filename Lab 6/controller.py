# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 21:48:34 2020

@author: Alex
"""


from random import randint, shuffle
from classifier import Classifier
from copy import deepcopy 


class Controller:
    
    def __init__(self, filename):
        self.__filename = filename
        self.__input = self.readData()
        
    def readData(self):
        inputData = []
        
        with open(self.__filename) as f:
            lines = f.readlines()
            for line in lines: 
                data = line.split(',')
                attr = [data[0]]
                for i in range(1, 5):
                    attr.append(int(data[i]))
                inputData.append(attr)
    
        #shuffle(inputData)        
        return inputData                
    
    
    def run(self):
        learnInput = deepcopy(self.__input)
        #learnInput.sort()
        testInput = []
        
        # split 80/20
        for i in range(125):
            #remove 125 entries and add to the testing sample (all data is read initially)
            index = randint(0, len(learnInput)-1)         
            testInput.append(learnInput[index])
            learnInput.remove(learnInput[index])
               
        classifier = Classifier()   
        tree = classifier.generateTree(learnInput)
        
        accuracy = 0
        for row in testInput: 
            predict = classifier.predict(row, tree)            
            if row[0] in predict:
                accuracy+=1

        return (float(accuracy) / len(testInput) * 100)
