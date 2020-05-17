# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:22 2020

@author: Alex
"""


class Problem:
    
    def __init__(self):
        self.texture={'very soft':set(),
                      'soft':set(),
                      'normal':set(),
                      'resistant':set()
                      }
        
        self.capacity={'small':set(),
                       'medium':set(),
                       'high':set()
                       }
        
        self.cycle={'delicate':set(),
                    'easy':set(),
                    'normal':set(),
                    'intense':set()
                    }      
        
        self.rules={'delicate':[],
                    'easy':[],
                    'normal':[],
                    'intense':[]
                    }     
        
        self.result={}
        
        self.__readTexture()
        self.__readCapacity()
        self.__readCycle()
        self.__readRules()
        
    def __readTexture(self):
        with open('data\\texture.txt','r') as f:
            pass
    
    def __readCapacity(self):
        with open('data\\capacity.txt','r') as f:
            pass
    
    def __readCycle(self):
        with open('data\\cycle.txt','r') as f:
            pass
    
    def __readRules(self):
        with open('data\\rules.txt','r') as f:
            lines = f.readlines()
            for line in lines:
                content = line.strip().split('-')
                self.rules[content[2]].append((content[0],content[1]))
    
