# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 19:08:45 2020

@author: Alex
"""

from qtpy.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QLineEdit, QLabel
import matplotlib.pyplot as plt 
from stats.Statistics import PSOStats
from domain.ParticleSwarmOptimisation import PSOThreaded

class ParticleSwarmAlgorithmWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(ParticleSwarmAlgorithmWindow, self).__init__(parent)
        self.__setupUI()
        self.__algoThreaded = PSOThreaded(1,1,1,1,1,1,1,1,1)
        self.__algoThreaded.signal.connect(self.status)
        self.__thread = PSOStats('data\\pso.in')
        self.__thread.signal.connect(self.received)
        
    def __setupUI(self):
        self.setWindowTitle('PSO')
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
        
        
        self.horizontalBox = QHBoxLayout()
        self.horizontalBox.addStretch(1)
        self.horizontalBox.addWidget(self.solutionButton)
        self.horizontalBox.addWidget(self.stopSolutionButton)
        self.horizontalBox.addWidget(self.statsButton)
        self.horizontalBox.addWidget(self.stopStatsButton)
        
        individualSizeBox = QHBoxLayout()
        label = QLabel("pop size:")
        self.problemSizeInput = QLineEdit()
        individualSizeBox.addWidget(label)
        individualSizeBox.addWidget(self.problemSizeInput)
        
        particleNoBox = QHBoxLayout()
        particleLabel = QLabel("No of particles (n):")
        self.particleNoInput = QLineEdit()
        particleNoBox.addWidget(particleLabel)
        particleNoBox.addWidget(self.particleNoInput)
        
        inertiaCoefBox = QHBoxLayout()
        inertiaLabel= QLabel("w:")
        self.inertiaInput = QLineEdit()
        inertiaCoefBox.addWidget(inertiaLabel)
        inertiaCoefBox.addWidget(self.inertiaInput)
        
        cognitiveCoefBox = QHBoxLayout()
        cognitiveLabel = QLabel("c1:")
        self.cognitiveInput = QLineEdit()
        cognitiveCoefBox.addWidget(cognitiveLabel)
        cognitiveCoefBox.addWidget(self.cognitiveInput)
        
        socialLearnBox = QHBoxLayout()
        socialLearnLabel = QLabel("c2:")
        self.socialLearnInput = QLineEdit()
        socialLearnBox.addWidget(socialLearnLabel)
        socialLearnBox.addWidget(self.socialLearnInput)
        
        neighbourhoodSizeBox = QHBoxLayout()
        neighbourhoodLabel = QLabel("neighbourhood size:")
        self.neighbourhoodInput = QLineEdit()
        neighbourhoodSizeBox.addWidget(neighbourhoodLabel)
        neighbourhoodSizeBox.addWidget(self.neighbourhoodInput)
        
        vMinSizeBox = QHBoxLayout()
        vMinLabel = QLabel("vmin:")
        self.vMinInput = QLineEdit()
        vMinSizeBox.addWidget(vMinLabel)
        vMinSizeBox.addWidget(self.vMinInput)
        
        vMaxSizeBox = QHBoxLayout()
        vMaxLabel = QLabel("vmax:")
        self.vMaxInput = QLineEdit()
        vMaxSizeBox.addWidget(vMaxLabel)
        vMaxSizeBox.addWidget(self.vMaxInput)
        
        gensBox = QHBoxLayout()
        gensLabel = QLabel("iterations:")
        self.numberOfGenerationsInput = QLineEdit()
        gensBox.addWidget(gensLabel)
        gensBox.addWidget(self.numberOfGenerationsInput)
        
        self.solutionLabel = QLabel()
        self.statsLabel = QLabel()
        self.verticalBox = QVBoxLayout()
        self.verticalBox.addStretch(1)
        self.verticalBox.addLayout(individualSizeBox)
        self.verticalBox.addLayout(particleNoBox)
        self.verticalBox.addLayout(inertiaCoefBox)
        self.verticalBox.addLayout(cognitiveCoefBox)
        self.verticalBox.addLayout(socialLearnBox)
        self.verticalBox.addLayout(neighbourhoodSizeBox)
        self.verticalBox.addLayout(vMinSizeBox)
        self.verticalBox.addLayout(vMaxSizeBox)
        self.verticalBox.addLayout(gensBox)
        self.verticalBox.addWidget(self.solutionLabel)
        self.verticalBox.addWidget(self.statsLabel)
        self.verticalBox.addLayout(self.horizontalBox)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.verticalBox)
        
        
    def __solutionButtonClicked(self):
        n = int(self.problemSizeInput.text())
        particleSize = int(self.particleNoInput.text())
        w = float(self.inertiaInput.text())
        c1 = float(self.cognitiveInput.text())
        c2 = float(self.socialLearnInput.text())
        neighbourhoodSize = int(self.neighbourhoodInput.text())
        iterations = int(self.numberOfGenerationsInput.text())
        vmin = int(self.vMinInput.text())
        vmax = int(self.vMaxInput.text())
        self.__algoThreaded = PSOThreaded(n, particleSize, w, c1, c2, vmin, vmax, neighbourhoodSize, iterations)
        self.__algoThreaded.signal.connect(self.status)
        self.__algoThreaded.start()
        self.stopSolutionButton.setEnabled(True)
        self.solutionButton.setEnabled(False)
      
    def status(self, data):
        if len(data)==3:
            self.solutionButton.setEnabled(True)
            self.solutionLabel.setText("Solution:\n" + str(data[0]) + "\nFitness:" + str(data[1]))
        else: 
            print("[PSO]Step: " + str(data[1]) + " Best fitness so far:" + str(data[0]))
   
    def __stopSolution(self):
        self.__algoThreaded.terminate()
        self.stopSolutionButton.setEnabled(False)
        self.solutionButton.setEnabled(True)
    
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
            print("[PSO]Step: " + str(data[1]) + " Best fitness so far:" + str(data[0]))
            

