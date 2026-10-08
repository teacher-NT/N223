import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox
)

app = QApplication([])


style_combo = """
    font-size: 22px;
    background-color: yellow;
    border: 2px solid black;
"""

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

        self.matn2 = QLabel("Taom tanlanmagan")
        self.matn2.setStyleSheet("""
                    font-size: 22px;
                    font-weight: bold;
                    color: black;
                """)
        self.vbox.addWidget(self.matn2)
        self.add_combo()

        self.btn1 = QPushButton("Tugmacha 1")
        self.btn1.setStyleSheet("""
            font-size: 20px;
            background-color: lightgreen;
            border: 2px solid black;
        """)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

        self.show()
    
    def add_combo(self):
        self.menu = QComboBox()
        self.menu.addItems(['Palov', 'Somsa', "Sho'rva", "Shashlik", "Manti"])
        self.menu.setStyleSheet(style_combo)
        self.menu.currentTextChanged.connect(self.set_food)
        self.vbox.addWidget(self.menu)

    def set_food(self):
        food = self.menu.currentText()
        self.matn2.setText(f"Savatingizda: {food}")


win = Window()
app.exec_()