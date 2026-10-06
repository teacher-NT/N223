# pip install PyQt5

import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel
)

app = QApplication([])

window = QWidget()
window.setWindowTitle("Dastur")
window.setGeometry(1400, 100, 400, 700)

matn1 = QLabel(window)
matn1.setText("Welcome to MyFirstApp")
matn1.setStyleSheet("font-size: 25px; color: blue;")
matn1.move(75, 50)
window.show()
app.exec_()