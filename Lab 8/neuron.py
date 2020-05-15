# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:06:00 2020

@author: Alex
"""

from random import random 

"""
Basic neuron class, with a number of inputs and an activation function.
"""
class Neuron:
    def __init__(self, inputs, activationFunction):
        self.activationFunction = activationFunction
        self.inputs = inputs 
        self.weights = [random() for i in range(self.inputs)]
        self.output = 0 
        
    def setWeights(self, new):
        self.weights = new
        
    def fireNeuron(self, inputs):
        u = sum([x*y for x,y in zip(inputs, self.weights)])
        self.output = self.activationFunction(u)
        return self.output 
        
    def __str__(self):
        return str(self.weights)