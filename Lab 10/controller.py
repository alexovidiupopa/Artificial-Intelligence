# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:38 2020

@author: Alex
"""

from algorithm import Algorithm 

class Controller:
    
    def __init__(self):
        self.algorithm = Algorithm()
        
    def jumpStep(self, start, stop, step):
        r = start
        while r <= stop:
            yield r
            r += step
    
    def run(self, texture, capacity): 
        r=0
        for k in sorted(self.algorithm.problem.result.keys()):
            for i in range(len(self.algorithm.problem.rules[k])):

                r =  min(self.algorithm.fuzzyTexture(texture,self.algorithm.problem.texture[self.algorithm.problem.rules[k][i][0]]),
                          self.algorithm.fuzzyCapacity(capacity,self.algorithm.problem.capacity[self.algorithm.problem.rules[k][i][1]]))
                
                if r!= 0 and r not in self.algorithm.problem.result[k]:
                    self.algorithm.problem.result[k].append(r)

           

        """
        points - list of points from the Cycle graphic,  of coordinates of type (x,y) where x=0,20,40,60,80,100
        """
        points=[]
        maximum = 0
        for k in sorted(self.algorithm.problem.result.keys()):
            if len(self.algorithm.problem.result[k]) > 0:
                maximum = max(self.algorithm.problem.result[k])
            for x in self.jumpStep(0,1,0.1):
                    res = self.algorithm.fuzzyTriangle(x, self.algorithm.problem.cycle[k])
                    if res > maximum:
                        res = maximum
                    if res != 0:
                        points.append((x,res))

        points = sorted(points)

        """
        indexes - a list of indexes which represents an element that should be deleted from points
        an element (x,y) should be deleted from the list if there is another element with the same x but larger y
        """
        indexes = []
        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                if points[i][0] == points[j][0] and points[i][1]>=points[j][1]:
                    indexes.append(j)
                if points[i][0] == points[j][0] and points[i][1] <= points[j][1]:
                    indexes.append(i)

        """
        we delete the elements from list - points with the indexes from list - indexes
        """
    
        indexes.reverse()
        for i in indexes:
            del points[i]
  
        numerator = 0
        denominator = 0

        for i in points:
            numerator += i[0]*i[1]
            denominator += i[1]
            
        res = numerator/denominator
        print("Cycle: "+str(round(res,2)))

        for k in self.algorithm.problem.result.keys():
            if len(self.algorithm.problem.result[k]) > 0:
                final = self.algorithm.fuzzyCycle(round(res,2),self.algorithm.problem.Cycle[k])
                if final!=0:
                    print("\t", k, ": ", str(round(final,2)))
        print("\n")
        