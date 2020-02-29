# -*- coding: utf-8 -*-
class CryptoGame:
    def __init__(self, attempts): 
        self.__attempts = attempts
        self.__first = None
        self.__second = None
        self.__result = None
        self.__sign = None
        self.__read()
    
        
    def __read(self):
        with open("crypto1.txt", 'r') as f:
            content = f.read().splitlines()
            self.__first = content[0]
            self.__sign = content[1]
            self.__second = content[2]
            self.__result = content[3]
    
    def trySolve(self):
        pass
