# -*- coding: utf-8 -*-
from Controller.Controller import Controller

class UserInterface:
    def __init__(self, ctrl):
        self.__ctrl = ctrl
        
    def __solveDfs(self):
        pass
    
    def __solveGreedy(self):
        pass
    
    def run(self):
        while True:
            cmd=input()
            if cmd=="dfs":
                self.__solveDfs()
            elif cmd=="greedy":
                self.__solveGreedy()
            elif cmd=="exit":
                return
            else:
                continue
