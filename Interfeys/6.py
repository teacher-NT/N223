import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)

app = QApplication([])


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1400, 100, 400, 700)
        self.setWindowTitle("Dastur")
        self.vbox = QVBoxLayout()

        self.matn1 = QLabel("Welcome to MyFirsApp")
        self.matn1.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: blue;
        """)
        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton("Tugmacha 1")
        self.btn1.setStyleSheet("""
            font-size: 20px;
            background-color: lightgreen;
            border: 2px solid black;
        """)
        self.vbox.addWidget(self.btn1)

        self.btn2 = QPushButton("Tugmacha 2")
        self.btn2.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        self.vbox.addWidget(self.btn2)

        self.btn3 = QPushButton("Tugmacha 3")
        self.btn3.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        self.vbox.addWidget(self.btn3)

        self.btn4 = QPushButton("Tugmacha 4")
        self.btn4.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        self.vbox.addWidget(self.btn4)

        self.setLayout(self.vbox)

        self.show()


win = Window()
app.exec_()