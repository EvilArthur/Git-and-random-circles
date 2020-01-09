import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import uic
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawing)
        self.flag = False

    def drawing(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.flag:
            d = randint(1, 300)
            qp.setBrush(QColor(randint(1, 255), randint(1, 255), randint(1, 255)))
            qp.drawEllipse(140, 140, d, d)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())