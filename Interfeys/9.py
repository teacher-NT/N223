import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt

style_matn1 = """
     font-size: 32px;
     font-weight: bold;
"""

style_btn1 = """
    font-size: 24px;
    color: {};
    background-color: {};
    border: 2px solid black;
    padding: 10px;
    border-radius: 20px; 
"""

class SecondWindow(QWidget):
    def __init__(self, main_):
        super().__init__()
        self.main = main_
        self.vbox = QVBoxLayout()
        self.setGeometry(1400, 100, 400, 700)

        self.matn1 = QLabel("About us")
        self.matn1.setStyleSheet(style_matn1)
        self.matn1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton("Back")
        self.btn1.setStyleSheet(style_btn1.format("white", "blue"))
        self.btn1.clicked.connect(self.back_main)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

        self.show()

    def back_main(self):
        self.main.show()
        self.hide()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setGeometry(1400, 100, 400, 700)

        self.matn1 = QLabel("Welcome to App")
        self.matn1.setStyleSheet(style_matn1)
        self.matn1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.vbox.addWidget(self.matn1)

        self.edit1 = QLineEdit()
        self.edit1.setFixedHeight(50)
        self.vbox.addWidget(self.edit1)

        self.btn1 = QPushButton("Open")
        self.btn1.setStyleSheet(style_btn1.format("black", "yellow"))
        self.btn1.clicked.connect(self.open_second)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

        self.show()

    def open_second(self):
        self.second = SecondWindow(self)
        self.second.show()
        self.hide()

app = QApplication([])
win = MainWindow()
app.exec_()
