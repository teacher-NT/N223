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
window.setStyleSheet("background-color: #edeca8;")

matn1 = QLabel(window)
matn1.setText("Welcome to Tasbeh")
matn1.setStyleSheet("font-size: 25px; color: blue;")
matn1.setFont(font1)
matn1.move(100, 50)


matn2 = QLabel(window)
matn2.setText("0")
matn2.setStyleSheet("font-size: 50px; color: green;")
matn2.move(175, 150)
matn2.setFixedWidth(200)

btn1 = QPushButton(window)
btn1.setText("Count")
btn1.setGeometry(120, 250, 150, 50)
btn1.setStyleSheet("""
    font-size: 20px;
    color: #e6281e;
    background-color: #73e84f;
    border: 2px solid black;
    border-radius: 20px;
""")

def func_btn():
    n = int(matn2.text()) + 1
    matn2.setText(str(n))

btn1.clicked.connect(func_btn)


btn2 = QPushButton(window)
btn2.setText("Reset")
btn2.setGeometry(120, 310, 150, 50)
btn2.setStyleSheet("""
    font-size: 20px;
    color: white;
    background-color: #e6281e;
    border: 2px solid black;
    border-radius: 20px;
""")

def func_btn2():
    matn2.setText("0")

btn2.clicked.connect(func_btn2)


window.show()
app.exec_()



# =========================================================================


# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton
# )
# from PyQt5.QtGui import QFont

# # ---- Ranglar palitrasi ----
# BG        = "#F5EFE0"   # fon
# TITLE     = "#1F4D3A"   # sarlavha
# COUNTER   = "#8A6A1F"   # raqam
# PRIMARY   = "#2E7D5B"   # Count tugmasi
# PRIMARY_H = "#256A4C"   # Count (hover)
# PRIMARY_P = "#1F4D3A"   # Count (bosilganda)
# ON_PRIM   = "#FFF8E7"   # Count matni
# SECOND    = "#E8DFC8"   # Reset tugmasi
# SECOND_H  = "#DDD2B3"   # Reset (hover)
# SECOND_P  = "#CFC29B"   # Reset (bosilganda)
# ON_SECOND = "#6B3E26"   # Reset matni
# BORDER    = "#1F4D3A"   # chegara

# font1 = QFont("Gabriola", 40)

# app = QApplication([])

# window = QWidget()
# window.setWindowTitle("Dastur")
# window.setGeometry(1400, 100, 400, 700)
# window.setStyleSheet(f"background-color: {BG};")

# matn1 = QLabel(window)
# matn1.setText("Welcome to Tasbeh")
# matn1.setStyleSheet(f"font-size: 25px; color: {TITLE};")
# matn1.setFont(font1)
# matn1.move(100, 50)

# matn2 = QLabel(window)
# matn2.setText("0")
# matn2.setStyleSheet(f"font-size: 50px; color: {COUNTER}; font-weight: bold;")
# matn2.move(175, 150)
# matn2.setFixedWidth(200)

# btn1 = QPushButton(window)
# btn1.setText("Count")
# btn1.setGeometry(120, 250, 150, 50)
# btn1.setStyleSheet(f"""
#     QPushButton {{
#         font-size: 20px;
#         color: {ON_PRIM};
#         background-color: {PRIMARY};
#         border: 2px solid {BORDER};
#         border-radius: 20px;
#     }}
#     QPushButton:hover {{ background-color: {PRIMARY_H}; }}
#     QPushButton:pressed {{ background-color: {PRIMARY_P}; }}
# """)

# def func_btn():
#     n = int(matn2.text()) + 1
#     matn2.setText(str(n))

# btn1.clicked.connect(func_btn)

# btn2 = QPushButton(window)
# btn2.setText("Reset")
# btn2.setGeometry(120, 310, 150, 50)
# btn2.setStyleSheet(f"""
#     QPushButton {{
#         font-size: 20px;
#         color: {ON_SECOND};
#         background-color: {SECOND};
#         border: 2px solid {BORDER};
#         border-radius: 20px;
#     }}
#     QPushButton:hover {{ background-color: {SECOND_H}; }}
#     QPushButton:pressed {{ background-color: {SECOND_P}; }}
# """)

# def func_btn2():
#     matn2.setText("0")

# btn2.clicked.connect(func_btn2)

# window.show()
# app.exec_()