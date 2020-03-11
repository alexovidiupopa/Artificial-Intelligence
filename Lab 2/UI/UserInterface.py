# -*- coding: utf-8 -*-
from Controller.Controller import Controller

class UserInterface:
    def __init__(self):
        self.__ctrl = None 
        
    def __solveDfs(self):
        solutions=self.__ctrl.dfs()
        if solutions == []:
            print("No solution")
        else:
            for sol in solutions:
                print(sol)
            
    def __solveGreedy(self):
        solution=self.__ctrl.greedy()
        if solution is None:
            print("No solution")
        else:
            print(solution)

    def run(self):
        print("Please input the number of queens:")
        n = int(input())
        self.__ctrl = Controller(n)
        while True:
            print("Select desired method (dfs/greedy) or exit to stop execution")
            cmd=input()
            if cmd=="dfs":
                self.__solveDfs()
            elif cmd=="greedy":
                self.__solveGreedy()
            elif cmd=="exit":
                return
            else:
                print("Wrong cmd")
                continue
