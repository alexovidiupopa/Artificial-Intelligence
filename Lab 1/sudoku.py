import random
import math
import itertools
class Sudoku:
    def __init__(self, attempts, filename):
        self.__attempts = attempts
        self.__board = self.__read(filename)
        
    def __read(self,filename):
        board = []
        with open(filename,'r') as fin:
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
                    row.append(random.randint(1,n)) #put a random value on each empty space
                else: 
                    row.append(self.__board[i][j])
            copy.append(row)
        return copy
    
    def __checkLines(self, board, numbers):
        for row in board: 
            if set(row)!=numbers:
                return False
        return True
    
    def __checkCols(self, board, numbers):
        for column in zip(*board):
            if set(column)!=numbers:
                return False
        return True
    
    def __checkBoxes(self, board, numbers):
        n=len(board)
        sqn = int(math.sqrt(n))
        for i in range(0,n,sqn):
            for j in range(0,n,sqn):
                elems=set()
                for row in board[i:i+sqn]:
                    for elem in row: 
                        elems.add(elem)
                if elems!=numbers:
                    return False
        return True
    
    def __check_sudoku(self,board):
        numbers=set()
        for i in range(1,len(board)+1):
            numbers.add(i)
        return self.__checkCols(board, numbers) and self.__checkLines(board, numbers) and self.__checkBoxes(board, numbers)
        
    def trySolve(self):
        for i in range(self.__attempts):
            potential=self.__solve()
            if self.__check_sudoku(potential): 
                return potential
        return None