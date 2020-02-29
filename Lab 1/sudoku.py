import random

class Sudoku:
    def __init__(self, attempts):
        self.__attempts = attempts
        self.__board = self.__read()
        
    def __read(self):
        board = []
        with open("sudoku.txt",'r') as fin:
            for line in fin:
                lineNrs=[]
                for nr in line.split(' '): 
                    lineNrs.append(int(nr))
                board.append(lineNrs)
        return board
            
    def __solve(self):
        n=len(self.__board)
        copy=[]       
        for i in range(n):
            row=[]
            for j in range(n):        
                if self.__board[i][j]==0:
                    row.append(random.randint(1,n))
                else: 
                    row.append(self.__board[i][j])
            copy.append(row)
        return copy
    
    def __check_sudoku(self,board) :
        numbers = set(range(1, len(board) + 1)) #1...n
        if (any(set(row) != numbers for row in board) or
            any(set(col) != numbers for col in zip(*board))) :
            return False
        return True
    
    def trySolve(self):
        for i in range(self.__attempts):
            potential=self.__solve()
            if self.__check_sudoku(potential): 
                return potential
        return None