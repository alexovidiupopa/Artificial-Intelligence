from copy import deepcopy

class State:
    
    def __init__(self,n):
        self.__values = [[0 for i in range(n)] for j in range(n)]
        self.__n = n
        
    def getValues(self):
        return self.__values
    
    def setValues(self, values):
        self.__values=values
        
    def __str__(self):
        ans=""
        for row in self.__values:
            ans+=str(row)
            ans+="\n"
        return ans
    
    def __eq__(self, other):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j]!=other.getValues()[i][j]:
                    return False
        return True
    
    def getNextStates(self):
        nextStates = []
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j]!=1 and self.canPlacePiece(i,j): #check if we can put a piece on the current spot
                    newBoard = deepcopy(self.__values) #we need to deepcopy in order to avoid any issues caused by reference modifications
                    newBoard[i][j]=1
                    newState = State(self.__n)
                    newState.setValues(newBoard)
                    nextStates.append(newState)
        return nextStates
    
    def canPlacePiece(self, row, col):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j]==1:
                    if i==row or j==col or abs(i-row)-abs(j-col)==0:  #check all constraints when trying to place (on line, on column, on diagonals)
                        return False
        return True
    
    def validBoard(self):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__values[i][j]==1 and not self.canPlacePiece(i,j): #check if a currently placed queen attacks other queens
                        return False
        return True
    
    
    
    