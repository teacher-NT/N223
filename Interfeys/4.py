# pip install PyQt5

import os
os.system("cls")
import json

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit
)
from PyQt5.QtGui import QFont

font1 = QFont("Gabriola", 40)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Dastur")
window.setGeometry(1400, 100, 400, 700)
window.setStyleSheet("background-color: #edeca8;")

matn1 = QLabel(window)
matn1.setText("Student search")
matn1.setStyleSheet("font-size: 25px; color: blue;")
matn1.setFont(font1)
matn1.move(100, 50)

edit1 = QLineEdit(window)
edit1.setGeometry(75, 100, 250, 50)
edit1.setStyleSheet("""
    font-size: 20px;
    background-color: #f0ee89;
""")
edit1.setPlaceholderText("🔍Ism kiriting...")


matn2 = QLabel(window)
matn2.setText("")
matn2.setStyleSheet("font-size: 25px; color: green;")
matn2.move(100, 150)
matn2.setFixedSize(200, 200)

btn1 = QPushButton(window)
btn1.setText("Search")
btn1.setGeometry(120, 350, 150, 50)
btn1.setStyleSheet("""
    font-size: 20px;
    color: #e6281e;
    background-color: #73e84f;
    border: 2px solid black;
    border-radius: 20px;
""")

def func_btn():
    with open("N223/Some/students.json") as file:
        data = json.load(file)
    name = edit1.text().lower()
    for i in data:
        if i['name'].lower() == name:
            matn2.setText(f"{i['name']}.\nyoshi: {i['age']}.\nManzil: {i['address']}")
            break
    else:
        matn2.setText("Topilmadi...")

btn1.clicked.connect(func_btn)


window.show()
app.exec_()
