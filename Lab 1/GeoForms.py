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
    
    def __rotate(self, form):
        rotationDir = {'R':'U','U':'R','D':'L','L':'D'}
        newPath=""
        rotate=random.randint(0,3)
        for character in form: #perform rotation<=> build new form  
            temp = character
            for i in range(rotate):
                temp = rotationDir[temp]
            newPath+=temp
        return newPath
    
    def __solve(self):
        dirx={'U':-1,'D':1,'L':0,'R':0}
        diry={'U':0,'D':0,'L':-1,'R':1}
        matrix=[[0 for i in range(self.__cols)] for j in range(self.__rows)]
        output=[[0 for i in range(self.__cols)] for j in range(self.__rows)]
        for k in range(self.__n):
            x=random.randint(0,self.__rows-1) #generate stuff
            y=random.randint(0,self.__cols-1)
            matrix[x][y]+=1
            output[x][y]=k+1
            marked=[(x,y)]
            newForm=self.__rotate(self.__forms[k])
            for d in newForm:#check for out of bounds placement for each square to be added
                if x+dirx[d]>=0 and x+dirx[d]<self.__rows and y+diry[d]>=0 and y+diry[d]<self.__cols:
                    x+=dirx[d]
                    y+=diry[d]
                    if (x,y) not in marked:
                        matrix[x][y]+=1                       
                        marked.append((x,y))
                    output[x][y]=k+1  
                else: #piece is out of bounds
                    return [[2]],[[2]]
        return matrix,output
        
    
    def trySolve(self):
        for i in range(self.__attempts):
            potential,result = self.__solve()
            if self.__check(potential):
                return result
        return None
