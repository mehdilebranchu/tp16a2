from PySide2.QtWidgets import *
import random

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles de l'isen Yncrea Ouest")
        self.setMinimumSize(500,300)
        self.layout = QVBoxLayout()
        self.__text = QLabel("CSI")
        self.button1 = QPushButton("changer de Cycle")
        self.cycles = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        self.layout.addWidget(self.__text)
        self.layout.addWidget(self.button1)
        self.button1.clicked.connect(self.change)
        self.setLayout(self.layout)

    def change(self):
        self.__text.setText(random.choice(self.cycles))

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
