# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:28 2020

@author: Alex
"""
from problem import Problem

class Algorithm:
    
    def __init__(self):
        self.problem = Problem()
        
    def fuzzyTrapezium(self, x, values):
        a=values[0]
        b=values[1]
        c=values[2]
        d=values[3]
        result = max(0,
                     min ((x - a) / (b - a),
                         1,
                         (d - x) / (d-c)))
        return result

    def fuzzyTriangle(self, x, values):
        a = values[0]
        b = values[1]
        c = values[2]
        result = max(0,
                     min((x - a) / (b - a),
                         (c - x) / (c - b)))
        return result
    
    def fuzzyTexture(self, x, values):
        if x<0.2 and values == self.problem.texture['very soft']:
            return 1.0
        if x>0.9 and values == self.problem.texture['resistant']:
            return 1.0
        return self.fuzzyTrapezium(x,values) 
    
    def fuzzyCapacity(self, x, values):
        if x<1 and values == self.problem.capacity['small']:
            return 1.0
        if x>4 and values == self.problem.capacity['high']:
            return 1.0
        return self.fuzzyTriangle(x,values)
        
    def fuzzyCycle(self, x, values):
        if x<0.2 and values == self.problem.cycle['delicate']:
            return 1.0
        if x>0.9 and values == self.problem.cycle['intense']:
            return 1.0
        return self.fuzzyTrapezium(x,values)
    
    