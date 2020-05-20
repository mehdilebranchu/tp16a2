from PySide2.QtWidgets import *
from random import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'isen Yncrea Ouest")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()
        self.__text = QLabel("CSI")
        self.button1 = QPushButton("changer de Cycle")
        self.layout.addWidget(self.__text)
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.buttonClicked())
        self.setLayout(self.layout)

    def buttonClicked(self):
        cycles = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        r = randint(0,len(cycles)-1)
        self.__text.setText(cycles[r])

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
