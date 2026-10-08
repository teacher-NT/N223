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

        self.matn1 = QLabel()
        self.matn1.setText("Welcome to MyFirsApp")
        self.matn1.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: blue;
        """)
        # self.matn1.setGeometry(20,20, 350, 50)
        self.vbox.addWidget(self.matn1)

        self.btn1 = QPushButton()
        self.btn1.setText("Tugmacha 1")
        self.btn1.setStyleSheet("""
            font-size: 20px;
            background-color: lightgreen;
            border: 2px solid black;
        """)
        # self.btn1.setGeometry(80, 80, 240, 50)
        self.vbox.addWidget(self.btn1)

        self.btn2 = QPushButton()
        self.btn2.setText("Tugmacha 2")
        self.btn2.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        # self.btn2.setGeometry(80, 80, 240, 50)
        self.vbox.addWidget(self.btn2)

        self.btn3 = QPushButton()
        self.btn3.setText("Tugmacha 3")
        self.btn3.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        # self.btn3.setGeometry(80, 80, 240, 50)
        self.vbox.addWidget(self.btn3)

        self.btn4 = QPushButton()
        self.btn4.setText("Tugmacha 4")
        self.btn4.setStyleSheet("""
                    font-size: 20px;
                    background-color: lightgreen;
                    border: 2px solid black;
                """)
        # self.btn4.setGeometry(80, 80, 240, 50)
        self.vbox.addWidget(self.btn4)

        self.setLayout(self.vbox)

        self.show()


win = Window()
app.exec_()