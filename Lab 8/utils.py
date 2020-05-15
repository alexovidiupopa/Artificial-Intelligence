# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:04:39 2020

@author: Alex
"""
class Utils:
    
    @staticmethod
    def linear(x,a=0.1,b=0):
        return a*x+b
    
    @staticmethod
    def linear_derivative(x,a=0.1,b=0):
        return a
    
    @staticmethod
    def readData():  
        data = []
        with open('data.txt', 'r') as f: 
            lines = f.readlines()
            for line in lines:
                split = line.split(' ')
                if len(split)==1: #skip empty lines
                    continue
                data.append([float(num) for num in split])    
        x=[]
        y=[]
        for line in data: 
            x.append(line[:-1])
            y.append([line[-1]])
        return x, y
