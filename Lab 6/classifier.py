# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:10:46 2020

@author: Alex
"""


"""
Note: tree is built using CART method, not C4.5 method.
For some reason, C4.5 with entropy resulted in a slightly smaller mean value.
"""


from utils import labelCount
from nodes import Node, Leaf, Decision


class Classifier:
    
    def giniIndex(self,entries):
        # gini index = 1 - sum(pj ^ 2), pj = probability of label j
        labels = labelCount(entries)
        probs = []
        for label in labels: 
            labelProbability = labels[label] / float(len(entries))
            probs.append(labelProbability**2)
        return 1-sum(probs) 
    
    
    
    def informationGain(self,left, right, impurity):
        # gain with gini = impurity - (p*gini(left) + (1-p)*gini(right)) 
        proportionLeft = float(len(left)) / (len(left) + len(right))
        proportionRight = 1-proportionLeft
        return impurity - proportionLeft * self.giniIndex(left) - proportionRight * self.giniIndex(right)
    
    
    
    def createPartition(self, entries, decision):
        # split the current entries into two lists regarding the decision result (left/right i.e. true/false)
        left_entries = []
        right_entries = []
        
        for entry in entries: 
            if decision.choose(entry):
                left_entries.append(entry)
            else:
                right_entries.append(entry)
                
        return left_entries, right_entries
    


    def getBestDecision(self,entries):
        maxGain = 0 # keep track of best gain and decision so far
        bestDecision = None 
        currentImpurity = self.giniIndex(entries)
        
        # foreach attribute
        for column in range(1,len(entries[0])): 
            
            values = set()
            for entry in entries:
                values.add(entry[column])
            
            # for each distinct attribute on a column, create a decision node splitting for that attribute on that column
            for attribute in values: 
                decision = Decision(column, attribute)
        
                # and then split by previously built decision
                left_entries, right_entries = self.createPartition(entries, decision) 
                if len(left_entries) == 0 or len(right_entries)==0:
                    continue 
                
                currentGain = self.informationGain(left_entries, right_entries, currentImpurity)
                if currentGain>=maxGain:
                    maxGain, bestDecision = currentGain, decision
        
        return maxGain, bestDecision 
    
    def generateTree(self,entries): 
        gain, decision = self.getBestDecision(entries)
        
        if gain == 0: # if we get no gain, we've reached a leaf
            return Leaf(entries)
        
        left_entries, right_entries = self.createPartition(entries, decision)
        
        # generate recursively for left and right branches
        left_branch = self.generateTree(left_entries)
        right_branch = self.generateTree(right_entries)
        
        # create a decision node containing the left and right branches
        # a tree is esentially a root node
        return Node(decision, left_branch, right_branch)
    
    # predict where a entry will end up in the tree
    def predict(self, entry, node):
        if isinstance(node, Leaf):
            return node.predictions  # if reached label, return the label and how many have reached there
        
        if node.decision.choose(entry):
            return self.predict(entry, node.left_branch)
        else:
            return self.predict(entry, node.right_branch)