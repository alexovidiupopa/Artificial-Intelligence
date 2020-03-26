# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:06:31 2020

@author: Alex
"""

from qtpy.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QLabel
import matplotlib.pyplot as plt 
from stats.Statistics import HCStats
from domain.HillClimbing import HCThreaded

class HillClimbingAlgorithmWindow(QMainWindow):
    def __init__(self, parent=None):
        super(HillClimbingAlgorithmWindow, self).__init__(parent)
        self.__setupUI()
        self.__algoThreaded = HCThreaded(1)
        self.__algoThreaded.signal.connect(self.status)
        self.__thread = HCStats('data\\hc.in')
        self.__thread.signal.connect(self.received)
        

    def __setupUI(self):
        self.setWindowTitle('HC')
        self.solutionButton = QPushButton('Solution', self)
        self.solutionButton.resize(self.solutionButton.sizeHint())  
        self.solutionButton.clicked.connect(self.__solutionButtonClicked)
        
        self.stopSolutionButton = QPushButton('Stop solution', self)
        self.stopSolutionButton.resize(self.stopSolutionButton.sizeHint())
        self.stopSolutionButton.clicked.connect(self.__stopSolution)
        self.stopSolutionButton.setEnabled(False)
        
        self.statsButton = QPushButton('Statistics', self)
        self.statsButton.resize(self.statsButton.sizeHint())
        self.statsButton.clicked.connect(self.__statsButtonClicked)
        
        self.stopStatsButton = QPushButton('Stop stats', self)
        self.stopStatsButton.resize(self.stopStatsButton.sizeHint())
        self.stopStatsButton.clicked.connect(self.__stopStats)
        self.stopStatsButton.setEnabled(False)
        
        individualSizeBox = QHBoxLayout()
        label = QLabel("individual size:")
        self.problemSizeInput = QLineEdit()
        individualSizeBox.addWidget(label)
        individualSizeBox.addWidget(self.problemSizeInput)
        
        
        self.horizontalBox = QHBoxLayout()
        self.horizontalBox.addStretch(1)
        self.horizontalBox.addLayout(individualSizeBox)
        self.horizontalBox.addWidget(self.solutionButton)
        self.horizontalBox.addWidget(self.stopSolutionButton)
        self.horizontalBox.addWidget(self.statsButton)
        self.horizontalBox.addWidget(self.stopStatsButton)
        
        self.solutionLabel = QLabel()
        self.statsLabel = QLabel()
        self.verticalBox = QVBoxLayout()
        self.verticalBox.addStretch(1)
        self.verticalBox.addWidget(self.solutionLabel)
        self.verticalBox.addWidget(self.statsLabel)
        self.verticalBox.addLayout(self.horizontalBox)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.verticalBox)
     
    def __solutionButtonClicked(self):
        self.__algoThreaded = HCThreaded(int(self.problemSizeInput.text()))
        self.__algoThreaded.signal.connect(self.status)
        self.__algoThreaded.start()
        self.stopSolutionButton.setEnabled(True)
        self.solutionButton.setEnabled(False)
        
    def __stopSolution(self):
        self.__algoThreaded.terminate()
        self.stopSolutionButton.setEnabled(False)
        self.solutionButton.setEnabled(True)
    
    def status(self, data):
        if len(data)==3:
            self.solutionButton.setEnabled(True)
            self.solutionLabel.setText("Solution:\n" + str(data[0]) + "\nFitness:" + str(data[1]))
        else: 
            print("[HC]Step: " + str(data[1]) + " Best fitness so far:" + str(data[0]))
            
    def __statsButtonClicked(self):
        self.statsButton.setEnabled(False)
        self.stopStatsButton.setEnabled(True)
        self.__thread.start()
        
    def __stopStats(self):
        self.__thread.terminate() 
        self.statsButton.setEnabled(True)
        self.stopStatsButton.setEnabled(False)
           
    def received(self, data):
        if len(data)==3:
            self.statsButton.setEnabled(True)
            self.stopStatsButton.setEnabled(False)
            self.statsLabel.setText("Std dev: " + str(data[0]) + "\nMean:" + str(data[1]))
            plt.plot(data[2])
            plt.show()
        else: 
            print("[HC]Step: " + str(data[1]) + " Best fitness so far:" + str(data[0]))
