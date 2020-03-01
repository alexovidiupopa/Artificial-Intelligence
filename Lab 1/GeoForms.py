# -*- coding: utf-8 -*-

import numpy as np
import random
import copy as cp

class GeoForms:
    
    def __init__(self,attempts):
        self.__attempts = attempts
        self.__rows = None
        self.__cols = None
        self.__n = None
        self.__forms=[]
        self.__read()
    
    def __read(self):
        with open("geof2.txt",'r') as f:
            firstLine = f.readline().split(' ')
            self.__rows = int(firstLine[0])
            self.__cols = int(firstLine[1])
            self.__n = int(firstLine[2])
            for i in range(self.__n):
                self.__forms.append(f.readline().strip('\n'))
        
    
    def __check(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])): 
                if matrix[i][j]>1:
                    return False
        return True
    
    def __solve(self):
        dirx={'U':-1,'D':1,'L':0,'R':0}
        diry={'U':0,'D':0,'L':-1,'R':1}
        matrix=[]
        for i in range(self.__rows): 
            line=[]
            for j in range(self.__cols):
                line.append(0)
            matrix.append(line)
        displayed=cp.deepcopy(matrix)
        r = {'R':'U','U':'R','D':'L','L':'D'}     
        for k in range(self.__n):
            x=random.randint(0,self.__rows-1)
            y=random.randint(0,self.__cols-1)
            matrix[x][y]+=1
            displayed[x][y]=k+1
            viz=[(x,y)]
            path=self.__forms[k]
            newPath=""
            rotate=random.randint(0,3)
            for ch in path: 
                c = ch
                for i in range(rotate):
                    c = r[c]
                newPath+=c
            for d in newPath:
                if x+dirx[d]>=0 and x+dirx[d]<self.__rows and y+diry[d]>=0 and y+diry[d]<self.__cols:
                    x+=dirx[d]
                    y+=diry[d]
                    if (x,y) not in viz:
                        matrix[x][y]+=1                       
                        viz.append((x,y))
                    displayed[x][y]=k+1  
                else:
                    return [[2]],[[2]]
        return matrix,displayed
        
    
    def trySolve(self):
        for i in range(self.__attempts):
            potential,result = self.__solve()
            if self.__check(potential):
                return result
        return None
