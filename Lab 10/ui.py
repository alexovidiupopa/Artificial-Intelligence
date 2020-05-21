# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:14:42 2020

@author: Alex
"""

from controller import Controller 

class UI:
   
    def __readInput(self):
        print("input the problem parameters")
        try: 
            tex = float(input("texture="))
            cap = float(input("capacity="))
            return (tex,cap)
        except TypeError:
            return None
        except ValueError:
            return None
        
    def __findCycle(self, texture, capacity): 
        c = Controller()
        c.run(texture,capacity)
        
    
    def run(self): 
        while True: 
            print("choose between read/exit")
            cmd = input()
            if cmd=="exit":
                return 
            else:
                (texture, capacity) = self.__readInput()
                if (texture, capacity) is None: 
                    continue
                else: 
                    self.__findCycle(texture, capacity)
        