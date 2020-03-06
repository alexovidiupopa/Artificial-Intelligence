# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:40:28 2020

@author: Alex
"""
from sudoku import Sudoku
from CryptoGame import CryptoGame
from GeoForms import GeoForms
class taskC:
    
    def __init__(self):
        self.__game=None
        
    def __sudoku(self):
        attempts=int(input())
        filename=input()
        self.__game = Sudoku(attempts,filename)
        result = self.__game.trySolve()
        if result is None: 
            print("No possible solution found in the given attempts")
        else: 
            for line in result: 
                print(line)
            
    def __crypt(self):
        attempts=int(input())
        filename=input()
        self.__game = CryptoGame(attempts,filename)
        result = self.__game.trySolve()
        if result is None: 
            print("No possible solution found in the given attempts")
        else: 
            print(result)
    
    def __geom(self):
        attempts=int(input())
        self.__game = GeoForms(attempts)
        result = self.__game.trySolve()
        if result is None: 
            print("No possible solution found in the given attempts")
        else: 
            for form in result:               
                print(form)
    
    def menu(self):
        while True:
            print(">>")
            cmd=input()
            if cmd=="1":
                self.__sudoku()
            elif cmd=="2":
                self.__crypt()
            elif cmd=="3":
                self.__geom()
            elif cmd=="stop":
                return
            else:
                continue

c = taskC()
c.menu()