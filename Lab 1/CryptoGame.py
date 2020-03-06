# -*- coding: utf-8 -*-
import random

class CryptoGame:
    def __init__(self, attempts, filename): 
        self.__attempts = attempts
        self.__first = None
        self.__second = None
        self.__result = None
        self.__sign = None
        self.__letters={}
        self.__read(filename)
                
    def __read(self,filename):
        with open(filename, 'r') as f:
            content = f.read().splitlines()
            self.__first = content[0]
            self.__sign = content[1]
            self.__second = content[2]
            self.__result = content[3]
            for letter in self.__first:
                self.__letters[letter]=-1
            for letter in self.__second:
                self.__letters[letter]=-1
            for letter in self.__result:
                self.__letters[letter]=-1
    
    def __buildValue(self, word):
        reverse = word[::-1]
        value = 0
        hexa = 1
        for letter in reverse:
            value+= self.__letters[letter] * hexa 
            hexa*=16
        return value
    
    def __checkZerosFirstLetters(self):
        if self.__letters[self.__first[0]] == 0 or self.__letters[self.__second[0]] == 0 or self.__letters[self.__result[0]] == 0: 
            return False #if any letter which is the first in a word has value 0=> fail
        return True

    def __check(self):
        first = self.__buildValue(self.__first)
        second = self.__buildValue(self.__second)
        result = self.__buildValue(self.__result)
        if self.__sign == "+":
            return first+second==result and self.__checkZerosFirstLetters() 
        elif self.__sign=="-":
            return first-second==result and self.__checkZerosFirstLetters()
        elif self.__sign=="*":
            return first*second==result and self.__checkZerosFirstLetters()
        
    def __toHexa(self):    
        hexa = {0:"0", 1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        for letter in self.__letters.keys():
            self.__letters[letter] = hexa[self.__letters[letter]]
        return self.__letters
    
    def __solve(self):
        for letter in self.__letters.keys():
            self.__letters[letter] = random.randint(0,15) #generate a random hexa value for each letter
        
    def trySolve(self):
        for i in range(self.__attempts):
            self.__solve()
            if self.__check():
                return self.__toHexa()   
        return None
