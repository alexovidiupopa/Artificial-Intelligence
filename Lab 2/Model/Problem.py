
class Problem:
    
    def __init__(self):
        self.__state = None
    
    @staticmethod
    def expand(state):
        for line in state.getValues():
            if 0 in line: #if we still have an empty position on a line, we can still try expanding
                return state.getNextStates()
        return []
    
    @staticmethod
    def solution(state):
        for line in state.getValues():
            if sum(line)!=1: #since we only explore valid solutions, we can just check that we have 1 queen on each line, because the diagonal/column constraints have already been checked along the way
                return False
        return True
        
    @staticmethod
    def heuristic(state):
        if not state.validBoard(): #if by some way we have an invalid board, the heuristic returns -infinity (shouldn't happen, but better safe than sorry)
            return -float('inf')
        cost=0
        values = state.getValues()
        n=len(values)
        for i in range(n):
            for j in range(n):
                if values[i][j]==1: #if not, it returns the number of queens on the board
                    cost+=1
        return cost
            