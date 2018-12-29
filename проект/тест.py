import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton


class Window1(QWidget):
    def __init__(self):
        super(Window1, self).__init__()
        self.setWindowTitle('Window1')
        self.resize(500, 500)
        self.resize(1000, 1000)
    def initUI(self):
        self.mbox = QGridLayout(self)
        
        self.chColor = []
        
        self.box1 = QGroupBox("Выберите город")
        self.vbox1 = QVBoxLayout()
        for i in range(3):
            button = QRadioButton(self.fcolors[i])
            self.chColor.append(button)
            self.vbox1.addWidget(button)
        self.box1.setLayout(self.vbox1)
        self.chColor[0].setChecked(True)
        self.mbox.addWidget(self.box1, 0, 0)
        self.btn = QPushButton("Применить")
        self.btn.clicked.connect(self.run)
        self.btn.clicked.connect(self.openwindow)
        self.mbox.addWidget(self.btn, 1, 0, 1, 3)
        self.edits = []
        for i in range(3):
            ledit = QLabel("          ")
            ledit.setStyleSheet("background-color: #FF0000; font-size: 35px")
            self.edits.append(ledit)
            self.mbox.addWidget(self.edits[i], i + 2, 0, 1, 3)

    def run(self):
         for i in range(1):
            for j in range(3):
                if self.chColor[i*3 + j].isChecked():
                    if j == 0:
                        self.edits[i].setStyleSheet("background-color: #FFFFFF; font-size: 35px")
                        self.edits[i+1].setStyleSheet("background-color: #0000FF; font-size: 35px")
                        self.edits[i+2].setStyleSheet("background-color: #FF0000; font-size: 35px")
                            
                    elif j == 1:
                        self.edits[i].setStyleSheet("background-color: #000000; font-size: 35px")
                        self.edits[i+1].setStyleSheet("background-color: #FF0000; font-size: 35px")
                        self.edits[i+2].setStyleSheet("background-color: #FFFF00; font-size: 35px")    
                    elif j == 2:
                        self.edits[i].setStyleSheet("background-color: #FFFFFF; font-size: 35px")
                        self.edits[i+1].setStyleSheet("background-color: #008000; font-size: 35px")
                        self.edits[i+2].setStyleSheet("background-color: #FF0000; font-size: 35px")




class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def show_window_1(self):
        self.w1 = Window1()
        self.w1.button.clicked.connect(self.show_window_2)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.show_window_1()
    sys.exit(app.exec_())
