import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class A(QMainWindow):
    def __init__(self):
        super().__init__()

        self.p = 0
        self.l = 0

        self.acceptDrops()
        self.setWindowTitle('Капча')
        self.setGeometry(500, 200, 620, 680)
        self.setStyleSheet("background-color: darkolivegreen;")

        self.pixmap1 = QPixmap('1.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(50, 20, 200, 200)
        self.label.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('5.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(220, 20, 370, 200)
        self.label.setPixmap(self.pixmap2)

        self.pixmap3 = QPixmap('3.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(400, 20, 550, 200)
        self.label.setPixmap(self.pixmap3)

        self.pixmap3 = QPixmap('4.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(50, 220, 200, 280)
        self.label.setPixmap(self.pixmap3)

        self.pixmap3 = QPixmap('2.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(220, 220, 370, 280)
        self.label.setPixmap(self.pixmap3)

        self.pixmap3 = QPixmap('6.jpg')

        self.label = QLabel(self)
        self.label.setGeometry(410, 220, 550, 280)
        self.label.setPixmap(self.pixmap3)




        self.b1 = QCheckBox("1", self)
        self.b1.move(50, 220)
        self.b1.stateChanged.connect(self.clickBox)
        self.b1.setStyleSheet('color: bisque')

        self.b2 = QCheckBox("2", self)
        self.b2.move(220, 220)
        self.b2.stateChanged.connect(self.clickBox2)
        self.b2.setStyleSheet('color: bisque')

        self.b3 = QCheckBox("3", self)
        self.b3.move(400, 220)
        self.b3.stateChanged.connect(self.clickBox)
        self.b3.setStyleSheet('color: bisque')

        self.b1 = QCheckBox("4", self)
        self.b1.move(50, 450)
        self.b1.stateChanged.connect(self.clickBox2)
        self.b1.setStyleSheet('color: bisque')

        self.b1 = QCheckBox("5", self)
        self.b1.move(220, 450)
        self.b1.stateChanged.connect(self.clickBox)
        self.b1.setStyleSheet('color: bisque')

        self.b1 = QCheckBox("6", self)
        self.b1.move(400, 450)
        self.b1.stateChanged.connect(self.clickBox2)
        self.b1.setStyleSheet('color: bisque')


        self.textbox = QLineEdit("ВЫБЕРИТЕ КАРТИНКИ С КОТИКАМИ", self)
        self.textbox.setFont(QFont("Arial", 20))
        self.textbox.move(50, 500)
        self.textbox.setGeometry(50, 500, 520, 70)
        self.textbox.setStyleSheet('color: bisque')
        self.textbox.setAlignment(Qt.AlignCenter)


        self.button = QPushButton('ВЫ РОБОТ?', self)
        self.button.setGeometry(50, 580, 520, 80)
        self.button.setStyleSheet('background-color: bisque')
        self.button.clicked.connect(self.click)

        self.show()

    def clickBox(self, state):

        if state == Qt.Checked:
            print('Checked')
            self.p += 1
        else:
            print('Unchecked')
            self.p -= 1
        self.show()

    def clickBox2(self, state):

        if state == Qt.Checked:
            print('Checked')
            self.l += 1
        else:
            print('Unchecked')
            self.l -= 1
        self.show()

    def click(self):
        print('button click')
        if self.p == 3 and self.l == 0:
            msg = QMessageBox()
            msg.setWindowTitle("ВЫ ЧЕЛОВЕК")
            msg.setText("ПОЗДРАВЛЯЕМ, ВЫ ЧЕЛОВЕК!")
            msg.setIcon(QMessageBox.Warning)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("ВЫ РОБОТ")
            msg.setText("ПОЗДРАВЛЯЕМ, ВЫ РОБОТ!")
            msg.setIcon(QMessageBox.Warning)

        msg.exec_()



app = QApplication(sys.argv)
mainWin = A()
mainWin.show()
sys.exit( app.exec_() )