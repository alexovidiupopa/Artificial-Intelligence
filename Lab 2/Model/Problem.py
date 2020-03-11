
class Problem:
    
    def __init__(self):
        self.__state = None
    
    @staticmethod
    def expand(state):
        for line in state.getValues():
            if 0 in line:
                return state.getNextStates()
        return []
    
    @staticmethod
    def solution(state):
        for line in state.getValues():
            if sum(line)!=1:
                return False
        return True
        
    @staticmethod
    def heuristic(state):
        if not state.validBoard():
            return -float('inf')
        cost=0
        values = state.getValues()
        n=len(values)
        for i in range(n):
            for j in range(n):
                if values[i][j]==1:
                    cost+=1
        return cost
            