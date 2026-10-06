# pip install PyQt5

import os
os.system("cls")

from random import choice

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)
from PyQt5.QtGui import QFont

font1 = QFont("Gabriola", 40)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Dastur")
window.setGeometry(1400, 100, 400, 700)

matn1 = QLabel(window)
matn1.setText("Welcome to MyFirstApp")
matn1.setStyleSheet("font-size: 25px; color: blue;")
matn1.setFont(font1)
matn1.move(100, 50)


matn2 = QLabel(window)
matn2.setText("")
matn2.setStyleSheet("font-size: 25px; color: green;")
matn2.move(100, 150)
matn2.setFixedWidth(200)

btn1 = QPushButton(window)
btn1.setText("Press me")
btn1.setGeometry(120, 250, 150, 50)
btn1.setStyleSheet("""
    font-size: 20px;
    color: #e6281e;
    background-color: #73e84f;
    border: 2px solid black;
    border-radius: 20px;
""")

def func_btn():
    names = ['Iftixor', 'Azizbek', 'Zayniddin', 'Shahboz']
    name  = choice(names)
    matn2.setText(name)

btn1.clicked.connect(func_btn)


window.show()
app.exec_()