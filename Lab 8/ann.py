# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:07:12 2020

@author: Alex
"""

from layers import Layer, FirstLayer
from copy import deepcopy

class ANN: 
    def __init__(self, structure, activationFunction, derivative, bias=False): 
        self.structure = structure[:]
        self.activationFunction = activationFunction
        self.derivate = derivative 
        self.bias = bias 
        self.noLayers = len(self.structure) 
        self.layers = [FirstLayer(self.structure[0], bias)]
        for i in range(1, self.noLayers):
            self.layers = self.layers + [Layer(self.structure[i-1], activationFunction, self.structure[i])]
    
    def feedForward(self, inputs):
        self.signal = inputs[:]
        if self.bias:
            self.signal.append(1)
        for l in self.layers:
            self.signal = l.forward(self.signal)
        return self.signal

    def backPropag(self, loss, learnRate):
        err = loss[:]
        delta = []
        currentLayer = self.noLayers-1
        newConfig = ANN(self.structure, self.activationFunction, self.derivate, self.bias)
        
        for i in range(self.structure[-1]):
            delta.append(err[i]*self.derivate(self.layers[-1].neurons[i].output))
            for r in range(self.structure[currentLayer-1]):
                newConfig.layers[-1].neurons[i].weights[r] = self.layers[-1].neurons[i].weights[r] + learnRate*delta[i]*self.layers[currentLayer-1].neurons[r].output
        
        for currentLayer in range(self.noLayers-2,0,-1):
            
            currentDelta = []
            for i in range(self.structure[currentLayer]):
                currentDelta.append(self.derivate(self.layers[currentLayer].neurons[i].output)*sum([self.layers[currentLayer+1].neurons[j].weights[i]*delta[j] for j in range(self.structure[currentLayer+1])]))
            
            delta = currentDelta[:]
            for i in range(self.structure[currentLayer]):
                for r in range(self.structure[currentLayer-1]):
                    newConfig.layers[currentLayer].neurons[i].weights[r] = self.layers[currentLayer].neurons[i].weights[r] + learnRate*delta[i]*self.layers[currentLayer-1].neurons[r].output
        
        self.layers=deepcopy(newConfig.layers)
        
        
    def computeLoss(self, u, t):
        loss = []
        out = self.feedForward(u)
        for i in range(len(t)):
            loss.append(t[i]-out[i])
        return loss[:]
    