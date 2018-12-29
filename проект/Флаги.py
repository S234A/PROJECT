import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtWidgets import QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap

class Image(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.initUI()
        
    def initUI(self):
  
        label = QLabel(self)
        pixmap = QPixmap(self.image)
        label.setPixmap(pixmap)
  
        self.resize(pixmap.width(), pixmap.height())
        self.setWindowTitle('Картинка')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.MainWindow()
     

        
    def MainWindow(self):

        self.setWindowTitle("Город - флаг")
        self.fcolors = ['Москва','Берлин','София']
        self.resize(400, 400)
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
        self.mbox.addWidget(self.btn, 1, 0, 1, 2)
        self.edits = []
        for i in range(3):
            ledit = QLabel("          ")
            self.edits.append(ledit)
            self.mbox.addWidget(self.edits[i], i + 2, 0, 1, 2)

        self.edits[0].setStyleSheet("background-color: #FFFFFF; font-size: 35px; border: 1px solid black")
        self.edits[1].setStyleSheet("background-color: #0000FF; font-size: 35px; border: 1px solid black")
        self.edits[2].setStyleSheet("background-color: #FF0000; font-size: 35px; border: 1px solid black")

        self.pixmap = QPixmap('москва_.png')
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.mbox.addWidget(self.lbl, 0, 1)

    def run(self):
        for i in range(1):
            for j in range(3):
                if self.chColor[i*3 + j].isChecked():
                    if j == 0:
                        self.edits[i].setStyleSheet("background-color: #FFFFFF; font-size: 35px; border: 1px solid black")
                        self.edits[i+1].setStyleSheet("background-color: #0000FF; font-size: 35px; border: 1px solid black")
                        self.edits[i+2].setStyleSheet("background-color: #FF0000; font-size: 35px; border: 1px solid black")
                        
                        self.pixmap.load('москва_.png')
                        self.lbl.setPixmap(self.pixmap)
                           
                    elif j == 1:
                        self.edits[i].setStyleSheet("background-color: #000000; font-size: 35px; border: 1px solid black")
                        self.edits[i+1].setStyleSheet("background-color: #FF0000; font-size: 35px; border: 1px solid black")
                        self.edits[i+2].setStyleSheet("background-color: #FFFF00; font-size: 35px; border: 1px solid black")
                       
                        self.pixmap.load('берлин_.PNG')
                        self.lbl.setPixmap(self.pixmap)
                           
                    elif j == 2:
                        self.edits[i].setStyleSheet("background-color: #FFFFFF; font-size: 35px; border: 1px solid black")
                        self.edits[i+1].setStyleSheet("background-color: #008000; font-size: 35px; border: 1px solid black")
                        self.edits[i+2].setStyleSheet("background-color: #FF0000; font-size: 35px; border: 1px solid black")
                       
                        self.pixmap.load('софия_.PNG')
                        self.lbl.setPixmap(self.pixmap)

    def MousePressEvent(self, event):
        x = event.x()
        y = event.y()
        if x in range(200, 400) and y in range(0, 100):
            self.image = Image('москва.png')
            self.image.show()

           
            hbox1 = QHBoxLayout(self)
            for i in range(1):
                for j in range(3):
                    if self.chColor[i*3 + j].isChecked():
                        if j == 0:
                            self.image = Image('москва.png')
                            self.image.show()
                            
                        elif j == 1:
                            self.image = Image('берлин.png')
                            self.image.show()
                        else:
                            self.image = Image('софия.png')
                            self.image.show()
              
if  __name__  ==  '__main__':
    app = QApplication(sys.argv)
    window = Window()    
    window.show()
    sys.exit(app.exec())

