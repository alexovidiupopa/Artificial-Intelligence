from Model.Problem import Problem
from Model.State import State
from copy import deepcopy

class Controller:
    
    def __init__(self,n):
        self.__instance = State(n)
        self.__root = State(n)
        self.__problem = Problem()
        
    def dfs(self):
        stack = [deepcopy(self.__root)]
        visited = []
        solutions = []
        while stack!=[]:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
            if Problem.solution(current):
                solutions.append(current)
            for expanded in Problem.expand(current):
                if expanded not in visited: 
                    visited.append(expanded)
                    stack = stack + [expanded]
        return solutions
    
    @staticmethod
    def order_states(states):
        return sorted(states, key=lambda state: Problem.heuristic(state), reverse=True)
      
    def greedy(self):
        queue = [deepcopy(self.__root)]
        visited=[]
        while queue!=[]:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
            if Problem.solution(current):
                return current
            for expanded in Problem.expand(current):
                if expanded not in visited: 
                    if Problem.solution(expanded):
                        return expanded
                    visited.append(expanded)
                    queue = [expanded] + queue
            queue = Controller.order_states(queue)
        return None
                