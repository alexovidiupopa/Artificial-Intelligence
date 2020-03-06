# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:28:56 2020

@author: Alex
"""

from Model.LatinSquare import LatinSquare
from UI.UserInterface import UserInterface
from Controller.Controller import Controller 

latinSquare = LatinSquare('res/in.txt')
ctrl = Controller(latinSquare)
console = UserInterface(ctrl)
console.run()