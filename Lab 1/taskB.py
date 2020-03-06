# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 20:43:00 2020

@author: Alex
"""
import random
import matplotlib.pyplot as plt
import numpy as np

class TaskB:
    def __init__(self):
        pass
        
    def __unif(self):
        a=int(input())
        b=int(input()) #interval [a,b]
        s = np.random.uniform(a,b,100)
        plt.plot(s, 'ro')
        plt.title('Uniform random numbers')
        plt.show()
        
    def __bino(self):
        n=int(input())
        p=float(input())  # number of trials, probability of each trial
        s = np.random.binomial(n, p, 100)
        plt.plot(s,'bo')
        plt.title('Bino distribution')
        plt.show()
        
    def __normal(self):
        mu, sigma = 0, 0.1 # mean and standard deviation
        s = np.random.normal(mu, sigma, 100)
        plt.plot(s,'bo')
        plt.title('Normal distribution')
        plt.show()
        
    def menu(self):
        while True:
            print(">>")
            cmd=input()
            if cmd=="unif":
                self.__unif()
            elif cmd=="bino":
                self.__bino()
            elif cmd=="normal":
                self.__normal()
            elif cmd=="stop":
                return
            else: 
                continue
            
task = TaskB()
task.menu()