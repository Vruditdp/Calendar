from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
print('ok') 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("  VRUDIT D PATEL ")
        self.setGeometry(100, 100, 600, 400)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        calender = QCalendarWidget(self)
        calender.setGeometry(10, 10, 400, 250)

        prev = QPushButton("Previous Year", self)
        prev.setGeometry(12, 280, 100, 40)
        prev.clicked.connect(lambda: do_revers_action())

        push = QPushButton("Next Year", self)
        push.setGeometry(310, 280, 100, 40)
        push.clicked.connect(lambda: do_action())

        def do_action():
            calender.showNextYear()

        def do_revers_action():
            calender.showPreviousYear()

App = QApplication(sys.argv)
window=Window()
sys.exit(App.exec())            