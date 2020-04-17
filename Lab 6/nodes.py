# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:53:15 2020

@author: Alex
"""

from utils import labelCount

class Leaf: 
    def __init__(self, entries):
        self.predictions = labelCount(entries)

class Node:
    def __init__(self, decision, left_branch, right_branch):
        self.decision = decision 
        self.left_branch = left_branch
        self.right_branch = right_branch 

class Decision:
    def __init__(self, column, attribute):
        self.column = column
        self.attribute = attribute

    def choose(self, other):
        attr = other[self.column]
        if self.column==1 or self.column==2:
            return attr>=self.attribute
        return attr<=self.attribute