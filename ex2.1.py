from PySide2.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("IHM")
        self.setMinimumSize(500,300)
        self.layout = QHBoxLayout
        self.Qbar = QProgressBar()
        self.slider = QSlider()
        self.layout.addWidget(self.Qbar)
        self.layout.addWidget(self.slider)





if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
