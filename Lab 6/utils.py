# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:31:42 2020

@author: Alex
"""

def labelCount(entries):
    # dictionary to hold pairs of <label> : <how_many> , i.e. {'R':25,'L':333} 
    count = {}
    for entry in entries: 
        if entry[0] not in count:            
            count[entry[0]]=1
        else:  
            count[entry[0]]+=1
    return count 