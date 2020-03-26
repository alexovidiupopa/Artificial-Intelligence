from qtpy.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow
from gui.EAWindow import EvolutionaryAlgorithmWindow
from gui.HCWindow import HillClimbingAlgorithmWindow
from gui.PSOWindow import ParticleSwarmAlgorithmWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.__setupUI()
        
    def __setupUI(self):  
        self.setWindowTitle('Home')
        self.evAlgorithmButton = QPushButton('EA', self)
        self.evAlgorithmButton.resize(self.evAlgorithmButton.sizeHint())   
        
        self.hillClimbButton = QPushButton('HC', self)
        self.hillClimbButton.resize(self.hillClimbButton.sizeHint())   

        self.particleSwarmButton = QPushButton('PSO')
        self.particleSwarmButton.resize(self.particleSwarmButton.sizeHint())
        
        self.horizontalBox = QHBoxLayout()
        self.horizontalBox.addStretch(1)
        self.horizontalBox.addWidget(self.evAlgorithmButton)
        self.horizontalBox.addWidget(self.hillClimbButton)
        self.horizontalBox.addWidget(self.particleSwarmButton)
        
        self.verticalBox = QVBoxLayout()
        self.verticalBox.addStretch(1)
        self.verticalBox.addLayout(self.horizontalBox)
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.verticalBox)

        self.evAlgorithmButton.clicked.connect(self.__evAlgorithmButtonClicked)
        self.hillClimbButton.clicked.connect(self.__hillClimbButtonClicked)
        self.particleSwarmButton.clicked.connect(self.__particleSwarmButtonClicked)
        
        self.evolutionaryAlgorithmWindow = EvolutionaryAlgorithmWindow(self)
        self.hillClimbingAlgorithmWindow = HillClimbingAlgorithmWindow(self)
        self.particleSwarmAlgorithmWindow = ParticleSwarmAlgorithmWindow(self)
        
    def __evAlgorithmButtonClicked(self):
        self.evolutionaryAlgorithmWindow.show()
        
    def __hillClimbButtonClicked(self):
        self.hillClimbingAlgorithmWindow.show()
        
    def __particleSwarmButtonClicked(self):
        self.particleSwarmAlgorithmWindow.show()
        