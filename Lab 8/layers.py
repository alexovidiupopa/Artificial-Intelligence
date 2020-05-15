# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:06:38 2020

@author: Alex
"""

from neuron import Neuron
from utils import Utils

class Layer:
    def __init__(self, noOfInputs, activationFunction, noOfNeurons):
        self.noOfNeurons = noOfNeurons
        self.neurons = [Neuron(noOfInputs, activationFunction) for i in 
                      range(self.noOfNeurons)]
        
    def forward(self, inputs):
        for x in self.neurons:
            x.fireNeuron(inputs)
        return([x.output for x in self.neurons])
        
    
class FirstLayer(Layer):
    def __init__(self, noOfNeurons, bias = False):
        if bias :
            noOfNeurons = noOfNeurons + 1
        Layer.__init__(self, 1, Utils.linear, noOfNeurons)
        for x in self.neurons:
             x.setWeights([1])
            
    def forward(self, inputs):
        for i in range(len(self.neurons)):
            self.neurons[i].fireNeuron([inputs[i]])
        return([x.output for x in self.neurons])