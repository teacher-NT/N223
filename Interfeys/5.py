import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)

app = QApplication([])

# win = QWidget()
# win.setGeometry(1400, 100, 400, 700)
# win.setWindowTitle("Dastur")

# matn1 = QLabel(win)
# matn1.setText("Welcome to MyFirsApp")
# matn1.setStyleSheet("""
#     font-size: 30px;
#     font-weight: bold;
#     color: blue;
# """)
# matn1.setGeometry(20,20, 350, 50)

# btn1 = QPushButton(win)
# btn1.setText("Tugmacha 1")
# btn1.setStyleSheet("""
#     font-size: 20px;
#     background-color: lightgreen;
#     border: 2px solid black;
# """)
# btn1.setGeometry(80, 80, 240, 50)

# win.show()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1400, 100, 400, 700)
        self.setWindowTitle("Dastur")

        self.matn1 = QLabel(self)
        self.matn1.setText("Welcome to MyFirsApp")
        self.matn1.setStyleSheet("""
            font-size: 30px;
            font-weight: bold;
            color: blue;
        """)
        self.matn1.setGeometry(20,20, 350, 50)

        self.btn1 = QPushButton(self)
        self.btn1.setText("Tugmacha 1")
        self.btn1.setStyleSheet("""
            font-size: 20px;
            background-color: lightgreen;
            border: 2px solid black;
        """)
        self.btn1.setGeometry(80, 80, 240, 50)

        self.show()


win = Window()
app.exec_()