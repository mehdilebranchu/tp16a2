from PySide2.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500,300)
        self.n = 0
        self.layout = QVBoxLayout()
        self.button1 = QPushButton("changez mon texte")
        self.text1 = QTextEdit("Nb click")
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.text1)
        self.setLayout(self.layout)
        #self.button1.clicked.connect(self.close)
        self.button1.clicked.connect(self.text)

    def text(self):
        self.n +=1
        self.button1.setText("click" + str(self.n))
        self.text1.setText("click" + str(self.n))
        print("click",self.n)

if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
