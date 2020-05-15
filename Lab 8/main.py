# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:49:04 2020

@author: Alex
"""
from statistics import mean
from utils import Utils
from ann import ANN
      
def main():
    nn = ANN([5,5,1],Utils.linear, Utils.linear_derivative)
    u, t = Utils.readData()  
    
    for i in range(100):   
        for j in range(len(u)):
            nn.backPropag(nn.computeLoss(u[j],t[j]), 0.01)
        
    # compute the errors
    diff = []    
    for i in range(len(u)):
        predicted = nn.feedForward(u[i])
        diff.append(abs(predicted[0]-t[i][0]))
        print("Actual: {}, Predicted:{}".format(t[i][0], predicted[0]))
        
    print("Mean of errors: {}".format(mean(diff)))
main()
    
