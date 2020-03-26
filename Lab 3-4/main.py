import sys
from qtpy.QtWidgets import QApplication
from gui.GUI import MainWindow
 

def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())    
    
run()
